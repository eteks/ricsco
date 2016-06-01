import time
from django.db import models
# from django.db.models import Q
from django.db.models.signals import pre_save, post_save
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# from django.conf import settings

from core.config import COUNTRIES, LANGUAGES
from reviews.models import Rating, Review
from ranks.models import Ranking

ACTOR_STATUS = (
    ('active', 'Active'),
    ('inactive', 'InActive'),
    ('test', 'Test'),
)
INVOICE_STATUS = (
    ('A', 'Applied'),
    ('D', 'Denied'),
    ('O', 'Approved'),              
)

class CompanyRating(Rating):
  """
  A Model to store Company rating information.
  Rating information is done by user.
  """
  reviews = models.ForeignKey('actors.CompanyReview', null=True, blank=True, help_text="Review for company")
  
class CompanyReview(Review):
  """
  A Model to store review information.
  Rating information is done for company.
  """
  pass

class CompanyRanking(Ranking):
  """
  A Model to store ranking information for Company.
  Ranking is done automatically by system.
  """
  ranking = models.ForeignKey('actors.CompanyRanking', null=True, blank=True, help_text="Ranking for company")

class ActorRating(Rating):  
  """
  A Model to store Actor rating information.
  Rating information is done by user.
  """
  reviews = models.ForeignKey('actors.ActorReview', null=True, blank=True, help_text="Ranking for the Actor")
    
class ActorReview(Review):
  """
  A Model to store review information.
  Rating information is done for actor.
  """
  pass

class ActorManager(models.Manager):
    def get_query_set(self):
        return (super(ActorManager, self).get_query_set().order_by('email'))
    
class ActorCompanyManager(models.Manager):
    def get_query_set(self):
        return (super(ActorCompanyManager, self).get_query_set().order_by('description'))
            
class ActorAddressManager(models.Manager):
    def get_query_set(self):
        return (super(ActorAddressManager, self).get_query_set().order_by('street'))

class CompanyAddressManager(models.Manager):
    def get_query_set(self):
        return (super(CompanyAddressManager, self).get_query_set().order_by('street'))

class AddressAbstract(models.Model):
  """
  A Meta Model to store Address information, Address model is always used with
  OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  
  street = models.CharField(max_length=512, default='gfdgdf', blank=True, help_text="Actor street full address information")
  postal_code = models.CharField(max_length=32, default='', blank=True, help_text="Some countries has characters in postal code, So keep the postal code in CharField")
  city = models.CharField(max_length=128, default='', null=True, help_text="Actor city information")
  state = models.CharField(max_length=128, default='', null=True, help_text="Actor state information")
  region = models.CharField(max_length=128, default='', blank=True, help_text="Use the overall term region, if both city and state is missing")
  
  country = models.CharField(max_length=3, default='', choices=COUNTRIES, help_text="Stored as ISO codes (SE, US, etc) in the DB. Check <a href='http://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO Countries</a> for ISO countries")
  # geotag = models.CharField(max_length=128, default='', null=True, help_text="Geo-tagging help users find a wide variety of location-specific information")
  modified_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system")
  created_on = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Auto generated by system")

  # latitude = models.FloatField(null=True, help_text="latitude of consumer address")
  # longitude = models.FloatField(null=True, help_text="longitude of consumer address")
  # geo_address = models.CharField(max_length=1024, null=True, help_text="Modified address to which latitude and longitude is identified") 
  # geo_location_status = models.CharField(max_length=16, choices=GEO_LOCATION_STATUS, null=True, default='notcalc', help_text="Status of Geo location")

  class Meta:
    abstract = True
    
  def clean(self):
    self.street = remove_none(self.street)
    self.postal_code = remove_none(self.postal_code)
    self.city = remove_none(self.city)
    self.state = remove_none(self.state)
    self.region = remove_none(self.region)
    self.country = remove_none(self.country)
  
  def save(self, *args, **kwargs):
    self.clean()
    super(AddressAbstract, self).save(*args, **kwargs)

  def location(self):
    if self.city:
      return "/".join([self.city, self.country])
    else:
      return "/".join([self.region, self.country])


  # def get_address_text(self):
  #   address_text = []

  #   if self.street:
  #     address_text.append(self.street)

  #   if self.city:
  #     address_text.append(self.city)

  #   if self.state:
  #     address_text.append(self.state)

  #   if self.region and (not self.city) and (not self.state):
  #     address_text.append(self.region)

  #   if self.postal_code:
  #     address_text.append(self.postal_code)

  #   if self.country:
  #     if self.country in COUNTRIES_DICT:
  #       address_text.append(COUNTRIES_DICT[self.country])
  #     else:
  #       address_text.append(self.country)

  #   if address_text:
  #     address_text =  ', '.join(address_text)
  #     if isinstance(address_text, unicode):
  #       return address_text.encode('utf-8') 

  #   return None

  @property
  def full_location(self):
    return self.__unicode__()

  def __unicode__(self):
    result = []
    if self.postal_code:
      result.append(self.postal_code)
    # if self.street:
    #   result.append(self.street)
    if self.city:
      result.append(self.city)
    if self.region and self.city.lower() != self.region.lower():
      result.append(self.region)
    if self.country:
      result.append(fixido_tags.country_name(self.country))
    return ', '.join(result)

class ActorAddress(AddressAbstract):
  """
  A Model to store Address information, Address model is always used with OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  objects = ActorAddressManager()
  
  class Meta:
    verbose_name = 'Actor address'
    verbose_name_plural = 'Actor addresses'
 
class CompanyAddress(AddressAbstract):
  """
  A Model to store Address information, Address model is always used with OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  objects = CompanyAddressManager()

  class Meta:
    verbose_name = 'Company address'
    verbose_name_plural = 'Company addresses'
  
class CompanyAbstract(models.Model):
  """
  Company instances are automatically created when user signed up, later admin have to approve the company 
  information to let others to add same company.
  """
  
  name = models.CharField(max_length=256, default='', blank=True, help_text="Company name")
  description = models.TextField(default='', blank=True, help_text="Company description")
  cin = models.CharField(max_length=32, default='', blank=True, help_text="Corporate identity number/Registration number")
  address = models.OneToOneField(CompanyAddress, null=True, blank=True, help_text="Company street full address information")
  phone_number = models.CharField(max_length=32, default='', blank=True, help_text="Company main phone number (Format: + and country-code eg +4670323435)")
  alt_phone_number = models.CharField(max_length=32, default='', blank=True, help_text="Company alternative phone number (Format: + and country-code eg +4670323435)")
  email = models.EmailField(max_length=75, default='', blank=True, help_text="Company contact email")
  website = models.URLField(max_length=200, default='', blank=True, help_text="Company website")
  logo = models.FileField(upload_to='logo', null=True, blank=True, help_text="Company logo uploaded to logotype directory") 
   
  rating = models.ForeignKey('actors.CompanyRating', null=True, blank=True, help_text="Rating to be provided by Actor towards company") 
  ranking = models.ForeignKey('actors.CompanyRanking', null=True, blank=True, help_text="Ranking to be generated by system automatically") 

  type = models.CharField(max_length=128, default='', blank=True, help_text="NOT IN USE")
  category = models.CharField(max_length=128, default='', blank=True, help_text="NOT IN USE")
  
  approved = models.BooleanField(default=False, help_text="Admin have to approve the company information to let others to add same company. NOT IN USE TODAY")
  
  # created_by = models.ForeignKey('actors.Actor', related_name='company_created', null=True, blank=True, help_text="Auto generated by system")
  created_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system")
  modified_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system")

  def __unicode__(self):
    return self.name if self.name else ''

  def clean(self):
    self.name = remove_none(self.name)
    self.description = remove_none(self.description)
    self.phone_number = remove_none(self.phone_number)
    self.alt_phone_number = remove_none(self.alt_phone_number)
    self.email = remove_none(self.email)
  
  def save(self, *args, **kwargs):
    self.clean()
    super(CompanyAbstract, self).save(*args, **kwargs)

class ActorCompany(CompanyAbstract):
  """
  A Model to store company information for actor.
  """
  objects = ActorCompanyManager()
  
  class Meta:
    verbose_name = 'Actor company'
    verbose_name_plural = 'Actor companies'

class Actor(User):
  """
  A Model to store Actors. An Actor can be both a seller or buyer of leads. 
  An Actor can also be a Fixido partner.
  An Actor can also belong to one partner.
  """  

  ssn = models.CharField(max_length=32, default='', blank=True, help_text="Social security number")

  address = models.OneToOneField(ActorAddress, null=True, blank=True, help_text="Actor full address information")
  
  phone_number = models.CharField(max_length=32, default='', blank=True, help_text="Actor main phone number (Format: + and country-code eg +4670323435)")
 
  alt_phone_number = models.CharField(max_length=32, default='', blank=True, help_text="Actor alternative phone number")
  alt_email = models.EmailField(default='', blank=True, help_text="Actor alternative email")
  skype = models.CharField(max_length=128, default='', blank=True, help_text="Actor Skype ID")
  twitter = models.CharField(max_length=128, default='', blank=True, help_text="Actor Twitter account")
  website = models.URLField(max_length=200, default='', blank=True, help_text="Actor Website URL")
  blog = models.URLField(max_length=200, default='', blank=True, help_text="Actor Blog URL")   
  linkedin_name = models.CharField(max_length=128, default='', blank=True, help_text="Actor LinkedIn account name") 
  linkedin_ref = models.CharField(max_length=128, default='', blank=True, help_text="Actor LinkedIn reference number")

  description = models.TextField(blank=True, help_text="More information about Actor")
    
  company = models.ForeignKey(ActorCompany, null=True, blank=True)  

  language = models.CharField(max_length=8, choices=LANGUAGES, default='', blank=True, help_text="Stored as ISO codes (Sv, En, etc) in the DB")
  timezone = models.CharField(max_length=10, default='UTC+01:00', blank=True, help_text="UTC TimeZone <a href='http://en.wikipedia.org/wiki/Time_zone' target='_blank'>(http://en.wikipedia.org/wiki/Time_zone)</a>, eg UTC+01:00 for London")
  invite_code = models.CharField(max_length=16, default='', blank=True, help_text="invite code")
  updated_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system")
  rating = models.ForeignKey('actors.ActorRating', null=True, blank=True, help_text="Rating done by User")
  lockout_times = models.CharField(max_length=10, default='', blank=True, help_text="lockout times")
    
  # def create_actor_number():
  #     try:
  #         return int(Actor.objects.order_by('-id')[0].actor_key) + 1
  #     except:
  #         return 5001

  # actor_key = models.CharField(max_length=128, default=create_actor_number, help_text="Actor unique key key used for identification")
  # secret_key = models.CharField(max_length=128, default=make_uuid, help_text="Actor unique secret key used to identify the Actor in API calls")
  # access_key = models.CharField(max_length=128, default=make_uuid, help_text="Actor unique access key used to identify the Actor in API calls")

  # confirmation_key = models.CharField(max_length=128, default=make_uuid, help_text="Registered user validate email")
  email_confirmation = models.BooleanField(default=False, help_text="To Check if User validated email")
    
  type = models.CharField(max_length=128, default='', blank=True, help_text="NOT IN USE")
  category = models.CharField(max_length=128, default='', blank=True, help_text="NOT IN USE")

  partner_status = models.BooleanField(default=False, blank=False, help_text="Describe whether the actor is partner of Fixido. If Actor is partner, True will be stored. False is the default value.")
  partner_commission = models.FloatField(default=0.0, help_text="Commission percentage allocated to Fixido partner")  
  # partner = models.ForeignKey('actors.Actor', related_name='partner_from', limit_choices_to = {"partner_status": "true"}, null=True, blank=True, help_text="This actor is connected to Fixido partner.")
  #To Check if User Logged in for the first time
  is_first = models.BooleanField(default=True, help_text="To Check if user logged in for the first time.")
  signup_method = models.CharField(max_length=128, default='', blank=True, help_text="Determine how the user is registered in Fixido")
  pkb_email = models.BooleanField(default=True, verbose_name='Send partner kickback email', help_text="To check e-mail should be sent to partner")

  email_subscribed = models.BooleanField(default=True, help_text="Subscribe to notice e-mail")
  sales_email = models.BooleanField(default=True, help_text="To check e-mail should be sent to seller")
  is_sellerregistered = models.BooleanField(default=False, help_text="To check if user registered for seller account.")
  
  Login_IPnumber = models.CharField(max_length=100, default='', blank=True, help_text="stores user ip when log in.")
  Registration_IPnumber = models.CharField(max_length=100, default='', blank=True, help_text="stores user ip when registration.")
  
  google_client_id = models.CharField(max_length=50, default='', blank=True, help_text="Google client ID.")
  seller_commission = models.FloatField(default=-1.0, help_text="Seller commission percentage. Standard 50, 40, 30 or -1 for 0 commission")

  # currency = models.CharField(max_length=6, 
  #   default=settings.BASE_CURRENCY, help_text="Actor's currency in ISO format")

  objects = ActorManager()
  
  class Meta:
    verbose_name = 'Actor'
    verbose_name_plural = 'Actors'

  def clean(self):
    self.first_name = remove_none(self.first_name)
    self.last_name = remove_none(self.last_name)
    self.language = remove_none(self.language)
    self.description = remove_none(self.description)
    self.phone_number = remove_none(self.phone_number)
    self.alt_phone_number = remove_none(self.alt_phone_number)
    self.email = remove_none(self.email)

  def save(self, force_insert=False, force_update=False):
    self.clean()
    self.username = self.email
    # if not self.currency:
    #   currency = settings.BASE_CURRENCY
      # if self.language and self.language in LANGUAGE_CURRENCIES:
      #   currency = LANGUAGE_CURRENCIES[self.language]
      # elif self.address and self.address.country and \
      #   self.address.country in COUNTRY_CURRENCIES:
      #   currency = COUNTRY_CURRENCIES[self.address.country]

      # self.currency = currency

    if not self.lockout_times:
      self.lockout_times = 0
    super(Actor, self).save(force_insert, force_update)


  @staticmethod
  def default_data():
    """
      This method will be called whenever the database is created (after syncdb)      
    """
    pass

def create_user(sender, instance, created, **kwargs):
    """
    Post Save Signal To Create Actor Details For Social Network User Login
    """    
    if created:
        user = User.objects.all().order_by('-id')[0]
        actor = Actor(user.pk)
        actor.username = user.username
        actor.first_name = user.first_name
        actor.last_name = user.last_name
        actor.email = user.email
        actor.save()

post_save.connect(create_user, sender=User)
  




  
