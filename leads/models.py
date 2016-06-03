import re
import logging

from collections import OrderedDict
from datetime import timedelta, datetime

from django.conf import settings
from django.db import models
from django.db.models import Q, F
from django.db.models.signals import pre_save, post_save
from django.utils.timezone import utc
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.exceptions import ValidationError

# from core import helper
from core.config import LANGUAGES
from actors.models import Actor, AddressAbstract, CompanyAbstract
from ranks.models import Ranking
# from haystack.query import SearchQuerySet
# from haystack.inputs import Clean, AutoQuery, Raw
# from worker.models import WorkerNoticeEmailTask
from ricsco.util import remove_none

LEADS_NEEDED_UNIT = (
    ('', 'None'),
    ('days', 'Days'),
    ('week', 'Week'),
    ('month', 'Month'),
    ('year', 'Year'),
)

LEAD_STATUS = (
    ('active', _('Active')),
    ('inactive', _('Inactive')),
    ('test', _('Test')),
)

LEAD_IMPORT_STATUS = (
    ('ok', 'OK'),
    ('error', 'error'),
)

LEAD_INACTIVE_REASON = (
    ('deal_done', _('Deal done')),
    ('deal_end', _('Deal end')),
    ('deal_withdrawn', _('Deal withdrawn')),
    ('duplicate', _('Duplicate')),
    ('moderate', _('Moderating')),
    ('old_lead', _('Old lead')),
    ('spam', _('Spam')),
    ('user_deleted', _('User deleted')),
)

GENDER = (
    ('unknown', 'Unknown'),
    ('male', 'Male'),
    ('female', 'Female'),
)

GENERATION_METHOD = (
    ('online', 'Online'),
    ('phone', 'Phone'),
)

LEAD_RANK = (
    (0.0, 0.0),
    (0.5, 0.5),
    (1.0, 1.0),
    (1.5, 1.5),
    (2.0, 2.0),
    (2.5, 2.5),
    (3.0, 3.0),
    (3.5, 3.5),
    (4.0, 4.0),
    (4.5, 4.5),
    (5.0, 5.0),
)

VERIFY_FIELD = (
    ('company', _('Company')),
    ('contact', _('Contact')),
    ('email', _('Email')),
    ('phone', _('Phone')),
    ('street', _('Street')),
)

VERIFY_STATUS = (
    ('ok', _('OK')),
    ('not_ok', _('Not OK')),
    ('missing', _('Missing')),
    ('error', _('Error')),
)

# AUCTION_STATUS = (
#   ('active', _('Active')),
#   ('inprogress', _('In progress')),
#   ('completed', _('Completed')),
#   ('nobid', _('No bid')),
# )

# BID_METHOD = (
#   ('manual', _('Manual')),
#   ('subscription', _('Subscription')),
# )

# BID_RESULT_STATUS = (
#   ('won', _('Auction won')),
#   ('lost', _('Auction lost')),
#   ('change', _('Bid changed')),
#   ('cancel', _('Bid cancelled')),
#   ('direct', _('Already bought')),
#   ('soldout', _('Sold out')),
#   ('inactive', _('Inactive lead')),
#   ('low', _('Low balance')),
#   ('provide', _('Provide lead')),
# )

ACTIVE_STATUS = (
    ('active', _('Active')),
    ('inactive', _('Inactive')),
)

class LeadManager(models.Manager):
    def get_query_set(self):
        return (super(LeadManager, self).get_query_set().order_by('title'))

class LeadCategoryManager(models.Manager):
    def get_query_set(self):
        return (super(LeadCategoryManager, self).get_query_set().order_by('name'))    

class ConsumerAddress(AddressAbstract):
  """
  Consumer address is where the lead consumer wants to be contacted
  """
  class Meta:
    verbose_name_plural = 'Consumer addresses'

  def save(self, force_insert=False, force_update=False):
    if self.id:
      old_text = ConsumerAddress.objects.get(pk=self.id).get_address_text()
      if old_text != self.get_address_text():
        self.geo_location_status = 'notcalc'

    super(ConsumerAddress, self).save(force_insert, force_update)


class ConsumerCompany(CompanyAbstract):
  """
  Consumer company is the company where the lead consumer works
  """
  industry = models.CharField(max_length=128, default='', blank=True, help_text="Industry type")  
  
  no_of_employees = models.CharField(max_length=50, default='', blank=True, help_text="Total number of employees")
  turn_over = models.IntegerField(default=0, blank=True, help_text="Total turn over")
  profit = models.IntegerField(default=0, blank=True, help_text="Total profit")
  company_financial_data_currency = models.CharField(max_length=8, default='', blank=True, help_text="Company financial data currency. Stored as ISO codes (SEK, EUR, etc) in the DB")
  
  visiting_address = models.OneToOneField(ConsumerAddress, null=True, blank=True, help_text="Visiting address (if not same as main company address)")  
  
  class Meta:
    verbose_name_plural = 'Consumer companies'

class Consumer(models.Model):
  """
  Consumer is the person requesting a product or service in a sales lead
  """
  first_name = models.CharField(max_length=256, default='', blank=True, help_text="First name of consumer.")
  last_name = models.CharField(max_length=256, default='', blank=True, help_text="Last name of consumer.")
  title = models.CharField(max_length=32, default='', blank=True, help_text="Title of consumer.")
  gender = models.CharField(max_length=10, default='unknown', choices=GENDER, blank=True, help_text="Gender of consumer.")
  
  email = models.EmailField(default='', blank=True, help_text="Email of consumer.")
  phone_number = models.CharField(max_length=16, default='', blank=True, help_text="Contact number of consumer.")
  alt_phone_number = models.CharField(max_length=16, default='', blank=True, help_text="Alternate contact number of consumer.")
  skype = models.CharField(max_length=128, default='', blank=True, help_text="Skype ID of consumer.")
  
  best_call_time = models.CharField(max_length=16, default='', blank=True, help_text="Best time to contact (call) the consumer.")
  preferred_method = models.CharField(max_length=16, default='', blank=True, help_text="Best method to contact the consumer (such as email/phone/visit).")
  
  address = models.OneToOneField(ConsumerAddress, null=True, blank=True, help_text="Address of consumer.")
  
  company = models.OneToOneField(ConsumerCompany, null=True, blank=True, help_text="Company  of consumer.") 
  position = models.CharField(max_length=32, default='', blank=True, help_text="Working position at current company.")   
  
  ssn = models.CharField(max_length=32, default='', blank=True, help_text="Social security number.")
  date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, help_text="Date of birth.")
  
  language = models.CharField(max_length=8, choices=LANGUAGES, default='', blank=True, help_text="Stored as ISO codes (Sv, En, etc) in the DB.")
  #TODO: PLEASE CHANGE THIS (AND ALL OTHER TIMEZONE FIELDS) TO SUPPORT DJANGO STANDARD TIMEZONE. 
  timezone = models.CharField(max_length=10, default='UTC+01:00', blank=True, help_text="PLEASE CHANGE THIS TO SUPPORT DJANGO STANDARD TIMEZONE. UTC TimeZone (http://en.wikipedia.org/wiki/Time_zone), eg UTC+01:00 for London.")
  
  updated_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
  
  info = models.TextField(blank=True, default='', help_text="Other consumer info")
  reference = models.CharField(max_length=32, default='', blank=True, help_text="Sellers reference number/id/site. Optional.")
    
  def clean(self):
    self.first_name = remove_none(self.first_name)
    self.last_name = remove_none(self.last_name)
    self.title = remove_none(self.title)
    self.gender = remove_none(self.gender)
    self.language = remove_none(self.language)
    self.phone_number = remove_none(self.phone_number)
    self.alt_phone_number = remove_none(self.alt_phone_number)
    self.email = remove_none(self.email)
    self.preferred_method = remove_none(self.preferred_method)
    self.reference = remove_none(self.reference)

  def save(self, *args, **kwargs):
    self.clean()
    super(Consumer, self).save(*args, **kwargs)

  def __unicode__(self):
    result = [] 
    if self.first_name:
      result.append(self.first_name)
    if self.last_name:
      result.append(self.last_name)
    if self.email:
      result.append(self.email)  
    if self.phone_number:
      result.append(self.phone_number)
    return ' '.join(result)
    #return self.first_name + " " + self.last_name


def lead_image_filepath(instance, filename):
  filename = str(time.time()).replace('.', '_') + '.jpg'
  filepath =  "/".join(['image', str(instance.seller.id), filename])
  return filepath

class Lead(models.Model):
  """
  Lead is a sales lead added by user
  """

  title = models.CharField(_('title'),max_length=256, default='', blank=True, help_text="Short title of the lead")
  description = models.TextField(default='', blank=True, help_text="Detailed description of the lead")
  read_more_link = models.URLField(max_length=200, default='', blank=True, help_text="A read more reference link (URL)")   
  image = models.ImageField(upload_to=lead_image_filepath, null=True, blank=True)

  price = models.DecimalField(verbose_name='Price', default=0.0, max_digits=10, decimal_places=2, help_text="Current price of lead")
  original_price = models.DecimalField(verbose_name='Original price', default=0.0, max_digits=10, decimal_places=2, help_text="Price of lead when added by seller")
  oldprice = models.DecimalField(verbose_name='Old price', default=0.0, max_digits=10, decimal_places=2, help_text="Price of lead before changed by admin")
  price_currency = models.CharField(max_length=8, default='', blank=True, help_text="Lead currency. Stored as ISO codes (SEK, EUR, etc) in the DB")

  sale = models.PositiveSmallIntegerField(default=0, help_text="Tells how many leads are originally available for sale")
  sold = models.PositiveSmallIntegerField(default=0, blank=True, help_text="Tells how many leads have been sold")
  pre_sold = models.PositiveSmallIntegerField(default=0, blank=True, help_text="Tells how many leads have been sold previously by the seller outside Fixido")

  seller = models.ForeignKey(Actor)
  reference = models.CharField(max_length=32, default='', blank=True, help_text="Sellers reference number/id/site. Optional.")
  consumer = models.ForeignKey(Consumer, null=True, blank=True, help_text="Consumer information for lead")
    
  deal_starts = models.DateTimeField(null=True, blank=True, help_text="Date from when the consumer wants to buy product or service")
  deal_ends = models.DateTimeField(null=True, blank=True, help_text="Date until when the consumer wants to buy product or service")
  budget = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, blank=True, help_text="Estimated total value of budget for the product/service")
  budget_currency = models.CharField(max_length=8, default='', blank=True, help_text="Budget currency. Stored as ISO codes (SEK, EUR, etc) in the DB")
    

  category = models.ForeignKey('leads.LeadCategory', null=True, blank=True, help_text="Category of leads")
  keywords = models.ManyToManyField('leads.LeadKeyword', blank=True)
  keywords.help_text = ""

  active = models.BooleanField(default=True, help_text="Lead status, handle by system")
  status = models.CharField(max_length=10, default='active', choices=LEAD_STATUS, help_text="Lead status, handle by seller")
  
  language = models.CharField(max_length=8, choices=LANGUAGES, default='', blank=True, help_text="Stored as ISO codes (Sv, En, etc) in the DB")
  timezone = models.CharField(max_length=10, default='UTC+01:00', blank=True, help_text="UTC TimeZone (http://en.wikipedia.org/wiki/Time_zone), eg UTC+01:00 for London")
  generation_method = models.CharField(max_length=128, default='online', choices=GENERATION_METHOD, blank=True, help_text="Specifies the method used to generate the lead")
  generation_source = models.CharField(max_length=256, default='', blank=True, help_text=" Tell us where the lead is generated")
  generation_date = models.DateTimeField(null=True, blank=True, help_text="Date when the lead was generated in sellers system")
  ranking = models.FloatField(choices=LEAD_RANK, default=0.0, blank=True, help_text="Ranking of leads")
  
  created = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
  modified = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")

  inactive_reason = models.CharField(max_length=100, choices=LEAD_INACTIVE_REASON, default='', null=False, blank=True, help_text="Reason to inactive this lead.")
  inactive_date = models.DateTimeField(null=True, blank=True, help_text="Auto generated by system.")
  accept_campaign = models.BooleanField(default=True, help_text="Can we use the lead in campaigns?")
  
  phone_verified = models.BooleanField(default=False, help_text="This lead is phone verified by Fixido.",verbose_name="PV")
  phone_verified_date = models.DateField(null=True, blank=True, help_text="Date of phone verification.")
  email_verified = models.BooleanField(default=False, help_text="This lead is email verified by Fixido.",verbose_name="EV")
  email_verified_date = models.DateField(null=True, blank=True, help_text="Date of email verification.")
  reinquire = models.BooleanField(default=False,verbose_name="RE")
  
  base_price = models.DecimalField(default=0.0, decimal_places=2,
    max_digits=10)
  base_currency = models.CharField(default=settings.BASE_CURRENCY, 
    max_length=6)
  # base_exchange_rate = models.DecimalField(default=1, decimal_places=4,
  #   max_digits=10)

  objects =  LeadManager()
  
  def __unicode__(self):
    return self.title if self.title else ''

  def isactive(self):
    if self.status == 'active' and self.active and self.sale > self.sold:
      return True
    return False

  # def price_as(self, currency):
  #   currency = currency.upper()

  #   if currency == self.base_currency:
  #     return self.base_price
  #   elif currency == self.price_currency:
  #     return self.price

  #   from commerce.models import CurrencyExchangeRate
  #   return CurrencyExchangeRate.Convert(self.base_price, 
  #     self.base_currency, currency)[0]

  # def budget_as(self, currency):

  #   currency = currency.upper()

  #   if currency == self.budget_currency:
  #     return self.budget

  #   from commerce.models import CurrencyExchangeRate
  #   return CurrencyExchangeRate.Convert(self.budget, 
  #     self.budget_currency, currency)[0]


  # def update_base_price(self, save=True):
  #   from commerce.models import CurrencyExchangeRate
  #   base_price, exchange_rate = CurrencyExchangeRate.ToBaseCurrency(
  #     self.price, self.price_currency)

  #   self.base_price = base_price
  #   self.base_exchange_rate = exchange_rate
  #   self.base_currency = CurrencyExchangeRate.BaseCurrency()

  #   if save:
  #     self.save()


  def clean(self):
    self.title = remove_none(self.title)
    self.description = remove_none(self.description)
    self.language = remove_none(self.language)
    self.generation_method = remove_none(self.generation_method)
    self.generation_source = remove_none(self.generation_source)

  def save(self, force_insert=False, force_update=False):
    self.clean()
    if self.original_price == 0:
      self.original_price = self.base_price    
    
    super(Lead, self).save(force_insert, force_update)

    if self.image:
      helper.image_resize(self.image)

    if hasattr(self, 'auction'):
      self.auction.save()

  def sell(self, actor, translation=None, order=None, quantity=1):
    """ Sells a single lead. It does not perform any e-commerce functionality 
        here. It updates dashboard, lead and folders.
    """

    from control.models import Folder, ActorBoughtLead
    # folder, created = Folder.objects.get_or_create(actor=actor, name="ALL")
    folder = None
    self.sold += quantity
    self.save()
    
    ActorBoughtLead(actor=actor, lead=self, folders=folder).save()

  @property
  def total(self):
    """Tells total number of leads"""
    return self.sale + self.pre_sold

  def available(self):
    """Tells how many leads are now available for sale (Leads left)"""
    return self.sale - self.sold

  def viewed(self):
    if not hasattr(self, 'leadstatistics'):
      LeadStatistics.objects.create(lead=self)
    
    self.leadstatistics.viewed += 1
    self.leadstatistics.save()

  @classmethod
  def get_related(cls, lead, count=10, minscore=0.1, debug=False, 
    fullobject=False, keywords_boost=0, title_boost=0,
    address_boost=0, by_recent=True, actor_language = None):
    
    if actor_language == "en":
      language_list = ["sv","en"]  
    else:
      language_list = [actor_language]

    base_query = dict(active = 1, status="active", language__in = language_list)
    qs =  SearchQuerySet().exclude(id=lead.id)
    if lead.keywords:
      keywords = lead.keywords.all().values_list('name', flat=True)
      if keywords:
        qs = qs.filter_or(keywords__in=keywords, **base_query)
        if keywords_boost != 0:
          qs = qs.boost('keywords', keywords_boost)

    if lead.consumer:
      address = []
      if lead.consumer.address:

        if lead.consumer.address.city:
          address.append(lead.consumer.address.city)
        if lead.consumer.address.region:
          address.append(lead.consumer.address.region)
        if lead.consumer.address.state:
          address.append(lead.consumer.address.state)
        if lead.consumer.address.country.strip():
          address.append(lead.consumer.address.country)

      if address:
        qs = qs.filter_or(address__in=address, **base_query)
        if address_boost != 0:
          qs = qs.boost('address', address_boost)

    if lead.title:
      title = re.sub(r'[^\w]', ' ', \
        lead.title, flags=re.UNICODE).split(' ')
      qs = qs.filter_or(title__in=title, **base_query)
      if title_boost != 0:
        qs = qs.boost('title', title_boost)  

    qs.models(Lead)
    qs.query.backend.default_operator = 'OR'

    if debug:
      print unicode(qs.query)

    if by_recent:
      related_leads = []
    
    i = 0
    for lead in qs:
      if lead.object:
        if lead.score > minscore:
          i += 1
          if by_recent:
            related_leads.append(lead)
          elif fullobject:
            yield lead
          else:
            yield (lead.object.id, lead.object)
        elif debug:
          print "ignored because of low score", lead.object.id, lead.score

        if i == count:
          break

    if by_recent and related_leads:
      related_leads.sort(cmp=lambda x, y: cmp(y.created, x.created))
      for lead in related_leads:
        if fullobject:
          yield lead
        else:
          yield (lead.object.id, lead.object)

def lead_save(sender, instance, **kwargs):
  # price = float(instance.price)
  status = instance.status
  status = status.lower()
  instance.status = status

  instance.update_base_price(save=False)


def copy_price(instance, created):
  if created:
    instance.original_price = instance.price
  
def create_worker_task(sender, instance, created, **kwargs):
  # this is not part of create worker task
  # To copy the price of lead to original price of lead
  copy_price(instance, created)
  
  mdays = settings.MAX_DAYS_TO_CREATE_WORKER_TASK
  create_task_from = helper.get_now() - timedelta(days=mdays)
  
  if instance.isactive() and instance.created.date() > create_task_from.date():
    WorkerNoticeEmailTask.create(instance)
  
# pre_save.connect(lead_save, sender=Lead)
# post_save.connect(create_worker_task, sender=Lead)


class LeadStatistics(models.Model):
  """Statistics of leads"""

  lead = models.OneToOneField(Lead)
  viewed = models.PositiveIntegerField(default=0, blank=True,
    help_text="Tells how many times the lead have been viewed")
  shared = models.PositiveIntegerField(default=0, blank=True,
    help_text="Tells how many times the lead have been shared")
  modified = models.DateTimeField(auto_now_add=True,
    help_text="Auto generated by system.")

  class Meta:
    verbose_name_plural = 'Lead statistics'

  def __unicode__(self):
    return str(self.pk)

class LeadRequest(models.Model):
  """
  LeadRequest is a request for lead added by user
  """
  buyer = models.ForeignKey(Actor)
  
  title = models.CharField(max_length=256, default='', blank=True, help_text="Short title of the request")
  description = models.TextField(default='', blank=True, help_text="Detailed description of the request")
  read_more_link = models.URLField(max_length=200, default='', blank=True, help_text="A read more reference link (URL)")   
  
  deal_starts = models.DateTimeField(null=True, blank=True, help_text="Date from when the consumer wants to buy product or service")
  deal_ends = models.DateTimeField(null=True, blank=True, help_text="Date until when the consumer wants to buy product or service")
  budget_min = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, blank=True, help_text="Minimum estimated total value of budget for the product/service")
  budget_max = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, blank=True, help_text="Maximum estimated total value of budget for the product/service")    
  budget_currency = models.CharField(max_length=8, default=settings.BASE_CURRENCY, blank=True, help_text="Min/Max budget currency. Stored as ISO codes (SEK, EUR, etc) in the DB")
    
  price_min = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, blank=True, help_text="Minimum price of requested leads")
  price_max = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, blank=True, help_text="Maximum price of requested leads")
  price_currency = models.CharField(max_length=8, default=settings.BASE_CURRENCY, blank=True, help_text="Min/Max lead price currency. Stored as ISO codes (SEK, EUR, etc) in the DB")

  rank_min = models.FloatField(default=0.0, blank=True, help_text="Minimum rank of requested leads")
  rank_max = models.FloatField(default=0.0, blank=True, help_text="Maximum rank of requested leads")
  
  category = models.ForeignKey('leads.LeadCategory', null=True, blank=True, help_text="One major category per lead")
  keywords = models.ManyToManyField('leads.LeadKeyword', blank=True, help_text="Multiple keywords related to the lead")
  
  leads_needed = models.CharField(max_length=16, default='', blank=True, help_text="Tells how many leads are requested from buyer")
  leads_needed_unit = models.CharField(max_length=10, default='', blank=True, choices=LEADS_NEEDED_UNIT, help_text="Tells what period the lead requested (eg. 100 leads per day). Values> day, week, month, year")
  
  viewed = models.PositiveIntegerField(default=0, blank=True, help_text="Tells how many times the request have been viewed")  
  shared = models.PositiveIntegerField(default=0, blank=True, help_text="Tells how many times the request have been shared")  
  
  active = models.BooleanField(default=True, help_text="Request status, handle by system")
  status = models.CharField(max_length=10, default='active', choices=LEAD_STATUS, help_text="Request status, handle by seller")
  
  location = models.CharField(max_length=128, default='', blank=True, help_text="Specifies in what location this is requested")
  # geotag = models.CharField(max_length=128, default='', blank=True, help_text="Geographical position specifying where this is requested")

  language = models.CharField(max_length=8, choices=LANGUAGES, default='', blank=True, help_text="Language of this request. Stored as ISO codes (Sv, En, etc) in the DB")
  timezone = models.CharField(max_length=10, default='UTC+01:00', blank=True, help_text="Timezone of this request. UTC TimeZone (http://en.wikipedia.org/wiki/Time_zone), eg UTC+01:00 for London")

  requested_language = models.ManyToManyField('leads.LeadRequestedLanguage', blank=True, help_text="Requested language. Stored as ISO codes (Sv, En, etc) in the DB")
  
  generation_method = models.CharField(max_length=128, default='', blank=True, help_text="Specified the method used to generate the request")

  created = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
  modified = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")


  def __unicode__(self):
    return self.title if self.title else ''

    
class LeadCategory(models.Model):
  name = models.CharField(max_length=128)
  parent = models.ForeignKey('self', null=True, blank=True)  
  objects = LeadCategoryManager()
  def create_actor_number():
      try:
          return int(LeadCategory.objects.order_by('-id')[0].category_number) + 1000
      except:
          return 1000
  
  category_number = models.CharField(max_length=128, default=create_actor_number, editable=True, help_text="automatically create category no used for api reference")
  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Lead categories'

class LeadKeyword(models.Model):
  name = models.CharField(max_length=128)
  
  def __unicode__(self):
    return self.name

  def __str__(self):
    return self.name

class KeywordStatistics(models.Model):
  name = models.CharField(max_length=128, editable=False)
  lead_count = models.PositiveIntegerField(default=0, editable=False, blank=True, help_text="Tells how many times the request have been shared")
  created = models.DateTimeField(auto_now_add=True, editable=False, help_text="Auto generated by system.")
  lead_language = models.CharField(max_length=8, editable=False, help_text="Identifies the language of lead.")
  
  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Keyword Statistics'

class Leadamount(models.Model):
  leadcount = models.BigIntegerField(default=0, editable=False, blank=True, help_text="Tells how many times the request have been shared")
  created = models.DateTimeField(auto_now_add=True, editable=False, help_text="Auto generated by system.")
  
  def __unicode__(self):
    return self.amount
  
class LeadRequestedLanguage(models.Model):
  name = models.CharField(max_length=8, choices=LANGUAGES, default='', blank=True, help_text="Stored as ISO codes (Sv, En, etc) in the DB")
  
  def __unicode__(self):
    return self.name
  
  
# class LeadImport(models.Model):
#   """
#   LeadImport is a log for all lead imports to the system
#   """
#   lead = models.ForeignKey(Lead)
#   actor = models.ForeignKey(Actor)
#   status_code = models.CharField(max_length=10, default='active', choices=LEAD_IMPORT_STATUS, help_text="Lead import status code, handle by system and returned in API calls")
#   message = models.CharField(max_length=128, default='', blank=True, help_text="Potential error message returned in API")
#   ip_address = models.CharField(max_length=128, default='', blank=True, help_text="Logged the IP address for the API call")
#   api_key = models.CharField(max_length=128, default='', blank=True, help_text="Logged the API key for the API call")   
#   created = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
#   modified = models.DateTimeField(auto_now_add=True, auto_now=True, help_text="Auto generated by system.")

#   def __unicode__(self):
#     return str(self.created)

class LeadVerification(models.Model):
  """ Lead lookup verification for contact, phone, email, company
  """
  lead = models.ForeignKey(Lead)
  source = models.CharField(max_length=128, default='', blank=True, help_text="Source used to verify.")
  field = models.CharField(max_length=128, choices=VERIFY_FIELD, default='', blank=True, help_text="Field verified.")
  status = models.CharField(max_length=10, choices=VERIFY_STATUS, default='', blank=True, help_text="Verified status.")
  verified_date = models.DateField(blank=True, null=True, help_text="Verified date.")
  created = models.DateField(auto_now_add=True, help_text="Auto generated by system.")
  modified = models.DateField(auto_now_add=True, help_text="Auto generated by system.")

  class Meta:
    verbose_name = 'Lookup verification'
    verbose_name_plural = 'Lookups verification'
    unique_together = ('lead', 'field')

  def __unicode__(self):
    return self.field.title()

def validate_minutes_to_start(minutes):
  """ Validation for minutes_to_auction_start field of Auction
  """
  error = _("Minutes to start auction should be greater than 600 minutes from now")
  if not minutes or minutes < 600:
    raise ValidationError(error)
    
class LeadAskQuestion(models.Model):
    lead = models.ForeignKey(Lead, blank=False, null=False)
    actor = models.ForeignKey(Actor, blank=True, null=True)
    email = models.EmailField(default='', blank=True, help_text="Email of user.")
    phone_number = models.CharField(max_length=16, default='', blank=True,null=True, help_text="Contact number of user.")
    question = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, help_text="Date and time of bid created.")
    website = models.CharField(max_length=150, blank=True)
   	# IPAddressField changed to GenericIPAddressField in django 1.8
    ipaddress = models.GenericIPAddressField(blank=True,null=True)
    # ipaddress = models.IPAddressField(blank=True)
