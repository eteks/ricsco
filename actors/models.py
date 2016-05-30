from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy, ugettext as _ 


COUNTRIES = (           
('','Select'), 
('AF',_('Afghanistan')),
('AX',_('Aland Islands Aland Islands')),
('AL',_('Albania')),
('DZ',_('Algeria')),
('AS',_('American Samoa')),
('AD',_('Andorra')),
('AO',_('Angola')),
('AI',_('Anguilla')),
('AQ',_('Antarctica')),
('AG',_('Antigua and Barbuda')),
('AR',_('Argentina')),
('AM',_('Armenia')),
('AW',_('Aruba')),
('AU',_('Australia')),
('AT',_('Austria')),
('AZ',_('Azerbaijan')),
('BS',_('Bahamas')),
('BH',_('Bahrain')),
('BD',_('Bangladesh')),
('BB',_('Barbados')),
('BY',_('Belarus')),
('BE',_('Belgium')),
('BZ',_('Belize')),
('BJ',_('Benin')),
('BM',_('Bermuda')),
('BT',_('Bhutan')),
('BO',_('Bolivia, Plurinational State of')),
('BQ',_('Bonaire, Sint Eustatius and Saba')),
('BA',_('Bosnia and Herzegovina')),
('BW',_('Botswana')),
('BV',_('Bouvet Island')),
('BR',_('Brazil')),
('IO',_('British Indian Ocean Territory')),
('BN',_('Brunei Darussalam')),
('BG',_('Bulgaria')),
('BF',_('Burkina Faso')),
('BI',_('Burundi')),
('KH',_('Cambodia')),
('CM',_('Cameroon')),
('CA',_('Canada')),
('CV',_('Cape Verde')),
('KY',_('Cayman Islands')),
('CF',_('Central African Republic')),
('TD',_('Chad')),
('CL',_('Chile')),
('CN',_('China')),
('CX',_('Christmas Island')),
('CC',_('Cocos (Keeling) Islands')),
('CO',_('Colombia')),
('KM',_('Comoros')),
('CG',_('Congo')),
('CD',_('Congo, the Democratic Republic of the')),
('CK',_('Cook Islands')),
('CR',_('Costa Rica')),
('CI',_('Cote dIvoire Cote dIvoire')),
('HR',_('Croatia')),
('CU',_('Cuba')),
('CW',_('Curacao Curacao')),
('CY',_('Cyprus')),
('CZ',_('Czech Republic')),
('DK',_('Denmark')),
('DJ',_('Djibouti')),
('DM',_('Dominica')),
('DO',_('Dominican Republic')),
('EC',_('Ecuador')),
('EG',_('Egypt')),
('SV',_('El Salvador')),
('GQ',_('Equatorial Guinea')),
('ER',_('Eritrea')),
('EE',_('Estonia')),
('ET',_('Ethiopia')),
('FK',_('Falkland Islands (Malvinas)')),
('FO',_('Faroe Islands')),
('FJ',_('Fiji')),
('FI',_('Finland')),
('FR',_('France')),
('GF',_('French Guiana')),
('PF',_('French Polynesia')),
('TF',_('French Southern Territories')),
('GA',_('Gabon')),
('GM',_('Gambia')),
('GE',_('Georgia')),
('DE',_('Germany')),
('GH',_('Ghana')),
('GI',_('Gibraltar')),
('GR',_('Greece')),
('GL',_('Greenland')),
('GD',_('Grenada')),
('GP',_('Guadeloupe')),
('GU',_('Guam')),
('GT',_('Guatemala')),
('GG',_('Guernsey')),
('GN',_('Guinea')),
('GW',_('Guinea-Bissau')),
('GY',_('Guyana')),
('HT',_('Haiti')),
('HM',_('Heard Island and McDonald Islands')),
('VA',_('Holy See (Vatican City State)')),
('HN',_('Honduras')),
('HK',_('Hong Kong')),
('HU',_('Hungary')),
('IS',_('Iceland')),
('IN',_('India')),
('ID',_('Indonesia')),
('IR',_('Iran, Islamic Republic of')),
('IQ',_('Iraq')),
('IE',_('Ireland')),
('IM',_('Isle of Man')),
('IL',_('Israel')),
('IT',_('Italy')),
('JM',_('Jamaica')),
('JP',_('Japan')),
('JE',_('Jersey')),
('JO',_('Jordan')),
('KZ',_('Kazakhstan')),
('KE',_('Kenya')),
('KI',_('Kiribati')),
('KP',_('Korea, Democratic People s Republic of')),
('KR',_('Korea, Republic of')),
('KW',_('Kuwait')),
('KG',_('Kyrgyzstan')),
('LA',_('Lao People s Democratic Republic')),
('LV',_('Latvia')),
('LB',_('Lebanon')),
('LS',_('Lesotho')),
('LR',_('Liberia')),
('LY',_('Libya')),
('LI',_('Liechtenstein')),
('LT',_('Lithuania')),
('LU',_('Luxembourg')),
('MO',_('Macao')),
('MK',_('Macedonia, The Former Yugoslav Republic of')),
('MG',_('Madagascar')),
('MW',_('Malawi')),
('MY',_('Malaysia')),
('MV',_('Maldives')),
('ML',_('Mali')),
('MT',_('Malta')),
('MH',_('Marshall Islands')),
('MQ',_('Martinique')),
('MR',_('Mauritania')),
('MU',_('Mauritius')),
('YT',_('Mayotte')),
('MX',_('Mexico')),
('FM',_('Micronesia, Federated States of')),
('MD',_('Moldova, Republic of')),
('MC',_('Monaco')),
('MN',_('Mongolia')),
('ME',_('Montenegro')),
('MS',_('Montserrat')),
('MA',_('Morocco')),
('MZ',_('Mozambique')),
('MM',_('Myanmar')),
('NA',_('Namibia')),
('NR',_('Nauru')),
('NP',_('Nepal')),
('NL',_('Netherlands')),
('NC',_('New Caledonia')),
('NZ',_('New Zealand')),
('NI',_('Nicaragua')),
('NE',_('Niger')),
('NG',_('Nigeria')),
('NU',_('Niue')),
('NF',_('Norfolk Island')),
('MP',_('Northern Mariana Islands')),
('NO',_('Norway')),
('OM',_('Oman')),
('PK',_('Pakistan')),
('PW',_('Palau')),
('PS',_('Palestinian Territory, Occupied')),
('PA',_('Panama')),
('PG',_('Papua New Guinea')),
('PY',_('Paraguay')),
('PE',_('Peru')),
('PH',_('Philippines')),
('PN',_('Pitcairn')),
('PL',_('Poland')),
('PT',_('Portugal')),
('PR',_('Puerto Rico')),
('QA',_('Qatar')),
('RE',_('Reunion !Reunion')),
('RO',_('Romania')),
('RU',_('Russian Federation')),
('RW',_('Rwanda')),
('BL',_('Saint Barthelemy !Saint Barthelemy')),
('SH',_('Saint Helena, Ascension and Tristan da Cunha')),
('KN',_('Saint Kitts and Nevis')),
('LC',_('Saint Lucia')),
('MF',_('Saint Martin (French part)')),
('PM',_('Saint Pierre and Miquelon')),
('VC',_('Saint Vincent and the Grenadines')),
('WS',_('Samoa')),
('SM',_('San Marino')),
('ST',_('Sao Tome and Principe')),
('SA',_('Saudi Arabia')),
('SN',_('Senegal')),
('RS',_('Serbia')),
('SC',_('Seychelles')),
('SL',_('Sierra Leone')),
('SG',_('Singapore')),
('SX',_('Sint Maarten (Dutch part)')),
('SK',_('Slovakia')),
('SI',_('Slovenia')),
('SB',_('Solomon Islands')),
('SO',_('Somalia')),
('ZA',_('South Africa')),
('GS',_('South Georgia and the South Sandwich Islands')),
('SS',_('South Sudan')),
('ES',_('Spain')),
('LK',_('Sri Lanka')),
('SD',_('Sudan')),
('SR',_('Suriname')),
('SJ',_('Svalbard and Jan Mayen')),
('SZ',_('Swaziland')),
('SE',_('Sweden')),
('CH',_('Switzerland')),
('SY',_('Syrian Arab Republic')),
('TW',_('Taiwan, Province of China')),
('TJ',_('Tajikistan')),
('TZ',_('Tanzania, United Republic of')),
('TH',_('Thailand')),
('TL',_('Timor-Leste')),
('TG',_('Togo')),
('TK',_('Tokelau')),
('TO',_('Tonga')),
('TT',_('Trinidad and Tobago')),
('TN',_('Tunisia')),
('TR',_('Turkey')),
('TM',_('Turkmenistan')),
('TC',_('Turks and Caicos Islands')),
('TV',_('Tuvalu')),
('UG',_('Uganda')),
('UA',_('Ukraine')),
('AE',_('United Arab Emirates')),
('GB',_('United Kingdom')),
('US',_('United States')),
('UM',_('United States Minor Outlying Islands')),
('UY',_('Uruguay')),
('UZ',_('Uzbekistan')),
('VU',_('Vanuatu')),
('VE',_('Venezuela, Bolivarian Republic of')),
('VN',_('Viet Nam')),
('VG',_('Virgin Islands, British')),
('VI',_('Virgin Islands, U.S.')),
('WF',_('Wallis and Futuna')),
('EH',_('Western Sahara')),
('YE',_('Yemen')),
('ZM',_('Zambia')),
('ZW',_('Zimbabwe')),
)
LANGUAGES = (
  ('',' '),            
  ('en', _('English')),
  ('en-UK', _('English - United Kingdom')),
  ('sv', _('Swedish')),
  ('da', _('Danish')),
  ('fi', _('Finish')),
  ('fr', _('French')),
  ('de', _('German')),
  ('it', _('Italian')),
  ('nn', _('Norwegian')),
  ('pl', _('Polish')),
  ('pt', _('Portuguese')),
  ('ru', _('Russian')),
  ('se', _('Spanish')), 
)

GEO_LOCATION_STATUS = (  
  ('notcalc', 'Not calculated'),
  ('wrong_address', 'Wrong Address'),
  ('identified', 'Identified'),  
)
class Review(models.Model):
  # """
  # A Meta Model to store Review information.
  # Reviews are for Leads and Seller. User will enter their review abou the Leads and seller are stored in different tables.
  # """
  actor = models.ForeignKey('actors.Actor', null=True)
  comments = models.CharField(max_length=512, blank=True)
  rating = models.PositiveSmallIntegerField(default=1)
  
  class Meta:
    abstract = True
    
  def __unicode__(self):
    return self.comments

class CompanyAddressManager(models.Manager):
    def get_query_set(self):
        return (super(CompanyAddressManager, self).get_query_set().order_by('street'))
class AddressAbstract(models.Model):
  """
  A Meta Model to store Address information, Address model is always used with
  OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  
  street = models.CharField(max_length=512, default='', blank=True, help_text="Actor street full address information")
  postal_code = models.CharField(max_length=32, default='', blank=True, help_text="Some countries has characters in postal code, So keep the postal code in CharField")
  city = models.CharField(max_length=128, default='', blank=True, help_text="Actor city information")
  state = models.CharField(max_length=128, default='', blank=True, help_text="Actor state information")
  region = models.CharField(max_length=128, default='', blank=True, help_text="Use the overall term region, if both city and state is missing")
  
  country = models.CharField(max_length=3, default='', choices=COUNTRIES, help_text="Stored as ISO codes (SE, US, etc) in the DB. Check <a href='http://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO Countries</a> for ISO countries")
  geotag = models.CharField(max_length=128, default='', blank=True, help_text="Geo-tagging help users find a wide variety of location-specific information")
  modified_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system")
  created_on = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Auto generated by system")

  latitude = models.FloatField(null=True, help_text="latitude of consumer address")
  longitude = models.FloatField(null=True, help_text="longitude of consumer address")
  geo_address = models.CharField(max_length=1024, null=True, help_text="Modified address to which latitude and longitude is identified") 
  geo_location_status = models.CharField(max_length=16, choices=GEO_LOCATION_STATUS, null=True, default='notcalc', help_text="Status of Geo location")

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


  def get_address_text(self):
    address_text = []

    if self.street:
      address_text.append(self.street)

    if self.city:
      address_text.append(self.city)

    if self.state:
      address_text.append(self.state)

    if self.region and (not self.city) and (not self.state):
      address_text.append(self.region)

    if self.postal_code:
      address_text.append(self.postal_code)

    if self.country:
      if self.country in COUNTRIES_DICT:
        address_text.append(COUNTRIES_DICT[self.country])
      else:
        address_text.append(self.country)

    if address_text:
      address_text =  ', '.join(address_text)
      if isinstance(address_text, unicode):
        return address_text.encode('utf-8') 

    return None

    
  def get_geolocation(self):
    if self.longitude and self.latitude:
      return Point(self.longitude, self.latitude)
    return None


  def identify_geolocation(self, geolocator=None, save=True):
    address = self.get_address_text()
    if address:
      geolocator = geolocator or GoogleV3()
      return geolocator.geocode(address)

    return None
  
  def update_geolocation(self, geolocator=None, save=True):
    address = self.get_address_text()
    if address:
      geolocator = geolocator or GoogleV3()

      try:
        address, (latitude, longitude) = geolocator.geocode(address)
        self.latitude = latitude
        self.longitude = longitude
        self.geo_address = address
        self.geo_location_status = 'identified'
      except (GQueryError, ValueError) as ge:
        self.latitude = None
        self.longitude = None
        self.geo_address = None        
        self.geo_location_status = 'wrong_address'
        print "Error while identity geopoint", ge, self.id
      except Exception, e:
        print "Unknown error while identity geopoint", e, type(e), self.id
        return None

      if save:
        self.save()


  @classmethod
  def proccess_recent_address(cls, limit=1500):
    """This functionality is moved to leads model to handle
    only active leads."""

    geolocator = GoogleV3()
    adds = cls.objects\
      .filter(
          Q(geo_location_status__isnull=True) \
          | Q(geo_location_status='notcalc'))\
      .order_by('-modified_on')[:limit]

    l = adds.count()
    
    i = 0
    for ad in adds:
      # print ad.get_address_text()
      ad.update_geolocation(geolocator=geolocator)
      i += 1 
      if i % 10 == 0:
        # Google API does not allow more request in short time, so 
        # sleep for two minutes
        time.sleep(2) 
        if i % 100 == 0:
          print "Processed %d(%d) of %s" %(i, l, cls)         


    return i

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
class CompanyAddress(AddressAbstract):
  """
  A Model to store Address information, Address model is always used with OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  objects = CompanyAddressManager()

  class Meta:
    verbose_name = 'Company address'
    verbose_name_plural = 'Company addresses'

class Rating(models.Model):
  """
  A Meta Model to store Rating information.
  Ratings are used for Leads and Seller. They are stored in different tables to keep separated.
  """
  name = models.CharField(max_length=128)
  rating = models.FloatField(default=0.0)
  
  class Meta:
    abstract = True
    
  def __unicode__(self):
    return self.name

'''Reviews are different opinions such as grading and comments added by users'''   

class Ranking(models.Model):
  """
  A Meta Model to store Ranking information.
  Rankings are used for Leads and Seller. They are stored in different tables to keep separated.
  """
  rank = models.FloatField(default=0.0)
  
  class Meta:
    abstract = True
    
  def __unicode__(self):
    return str(self.rank)

class CompanyReview(Review):
  """
  A Model to store review information.
  Rating information is done for company.
  """
  pass

class CompanyRating(Rating):
  """
  A Model to store Company rating information.
  Rating information is done by user.
  """
  reviews = models.ForeignKey('actors.CompanyReview', null=True, blank=True, help_text="Review for company")

class CompanyRanking(Ranking):
  """
  A Model to store ranking information for Company.
  Ranking is done automatically by system.
  """
  ranking = models.ForeignKey('actors.CompanyRanking', null=True, blank=True, help_text="Ranking for company")

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
  
  created_by = models.ForeignKey('actors.Actor', related_name='company_created', null=True, blank=True, help_text="Auto generated by system")
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


class ActorAddressManager(models.Manager):
    def get_query_set(self):
        return (super(ActorAddressManager, self).get_query_set().order_by('street'))
# Create your models here.
class AddressAbstract(models.Model):
  """
  A Meta Model to store Address information, Address model is always used with
  OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  
  street = models.CharField(max_length=512, default='', blank=True, help_text="Actor street full address information")
  postal_code = models.CharField(max_length=32, default='', blank=True, help_text="Some countries has characters in postal code, So keep the postal code in CharField")
  city = models.CharField(max_length=128, default='', blank=True, help_text="Actor city information")
  state = models.CharField(max_length=128, default='', blank=True, help_text="Actor state information")
  region = models.CharField(max_length=128, default='', blank=True, help_text="Use the overall term region, if both city and state is missing")
  
  country = models.CharField(max_length=3, default='', choices=COUNTRIES, help_text="Stored as ISO codes (SE, US, etc) in the DB. Check <a href='http://en.wikipedia.org/wiki/ISO_3166-1' target='_blank'>ISO Countries</a> for ISO countries")
  geotag = models.CharField(max_length=128, default='', blank=True, help_text="Geo-tagging help users find a wide variety of location-specific information")
  modified_on = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system")
  created_on = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Auto generated by system")

  latitude = models.FloatField(null=True, help_text="latitude of consumer address")
  longitude = models.FloatField(null=True, help_text="longitude of consumer address")
  geo_address = models.CharField(max_length=1024, null=True, help_text="Modified address to which latitude and longitude is identified") 
  geo_location_status = models.CharField(max_length=16, choices=GEO_LOCATION_STATUS, null=True, default='notcalc', help_text="Status of Geo location")

  class Meta:
    abstract = True

class ActorAddress(AddressAbstract):
  """
  A Model to store Address information, Address model is always used with OneToOne relationship.
  Addresses are used for Actors, Companies, Consumers and stored in different tables to keep separated.
  """
  objects = ActorAddressManager()
  
  class Meta:
    verbose_name = 'Actor address'
    verbose_name_plural = 'Actor addresses'
    
class ActorCompanyManager(models.Manager):
    def get_query_set(self):
        return (super(ActorCompanyManager, self).get_query_set().order_by('name'))

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
  class Meta :
    verbose_name_plural = 'Actors'
class Rating(models.Model):
  """
  A Meta Model to store Rating information.
  Ratings are used for Leads and Seller. They are stored in different tables to keep separated.
  """
  name = models.CharField(max_length=128)
  rating = models.FloatField(default=0.0)

class ActorRating(Rating):  
  # """
  # A Model to store Actor rating information.
  # Rating information is done by user.
  # """
  reviews = models.ForeignKey('actors.ActorReview', null=True, blank=True, help_text="Ranking for the Actor")

class ActorReview(Review):
  # """
  # A Model to store review information.
  # Rating information is done for actor.
  # """
  pass
