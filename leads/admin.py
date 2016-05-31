from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from models import *
from django.utils.translation import ugettext_lazy as _
# from control.models import ActorProvidedLead
from actors.models import Actor
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404

class ConsumerAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number')
  list_filter = ['timezone', 'language']
  search_fields = [
      'id', 'info', 'first_name', 'last_name', 'email', 'phone_number','lead__id','lead__title',
  ]
  fieldsets = [
      ('Basics',            {'fields': ['first_name', 'last_name']}),         
      (None,                {'fields': ['title']}),
      (None,                {'fields': ['gender']}),      
      (None,                {'fields': ['ssn']}),
      (None,                {'fields': ['date_of_birth']}),      
      (None,                {'fields': ['address']}),  
      (None,                {'fields': ['company']}),  
      (None,                {'fields': ['position']}),  
      ('Contact information', {'fields': ['email', 'phone_number','alt_phone_number','skype'],}),
      (None,                {'fields': ['best_call_time', 'preferred_method']}),      
      ('Localization',      {'fields': ['language','timezone']}),                                    
     # ('Date information',  {'fields': ['updated_on']}),
      ('All other info',    {'fields': ['info']}),            
  ]
  readonly_fields = ('address', 'company', )
  
class SellerListFilter(SimpleListFilter):
    title = _('seller')
    parameter_name = 'seller'
    def lookups(self, request, model_admin):
        sellers = Actor.objects.filter(is_sellerregistered=True)
        return [(seller, seller) for seller in sellers]
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(seller__email=self.value)
                
class LeadVerificationInline(admin.TabularInline):
    model = LeadVerification
    extra = 1
    max_num = 5
    readonly_fields = ('created', 'modified',)
    fields = (
      'source', 'field', 'status', 'verified_date', 'created', 'modified',
    )

class LeadAdmin(admin.ModelAdmin):
  
  class Media:
    js = ['admin/js/list_filter_collapse.js']
  
  ordering = ('-created',)
  list_display = (
    'id', 'title', 'seller', 'base_price', 'available', 'sale', 'sold', 
    'viewed_stats', 'email_sent', 'phone_verified', 'email_verified',
    'reinquire', 'language', 'created', 'status', 'active',
  )
  list_filter = ['active', 'status', 'inactive_reason', 'language', 
    SellerListFilter]
  search_fields = ['id', 'title', 'base_price', 'description', 'seller__email']
  # actions = ['export_csv', 'identify_geolocation','moderation_to_active']
  actions = ['export_csv','moderation_to_active']
  date_hierarchy = 'created'
  inlines = [LeadVerificationInline, ]

  fieldsets = [
      ('Basics',            {'fields': ['title']}),
      (None,                {'fields': ['description']}),
      (None,                {'fields': ['image','read_more_link']}),
      ('Price',             {'fields': ['price', 'price_currency', 'base_price',
                                        'base_currency','original_price', 
                                        'oldprice', ]}),
      ('Amount',            {'fields': ['available', 'sale', 'sold', 'pre_sold',
                                        'total']}),
      ('Seller',            {'fields': ['seller'],}),
      ('Reference',         {'fields': ['reference'],}),
      ('Consumer',          {'fields': ['consumer'],}),
      ('Deal information',  {'fields': ['deal_starts', 'deal_ends']}),
      (None,                {'fields': ['budget', 'budget_currency']}),
      ('Classification',    {'fields': ['category']}),
      (None,                {'fields': ['keywords']}),
      ('Localization',      {'fields': ['language','timezone']}),
      ('Tacking',           {'fields': ['generation_method',
                                        'generation_source']}),
      ('Date information',  {'fields': ['generation_date']}),
      ('Ranking',           {'fields': ['ranking'], 
                             'description': 'Ranking is done by system'}),
      ('System status',     {'fields': ['active', 'inactive_reason',
                                        'inactive_date']}),
      ('Actor status',      {'fields': ['status', 'accept_campaign',
                                        'reinquire']}),
      ('Verification',      {'fields': [
                                        'phone_verified', 'phone_verified_date',
                                        'email_verified', 'email_verified_date',
      ]}),
      ('Created',           {'fields': ['created', 'modified']}),
  ]
  readonly_fields = ( 'created', 'modified', 'keywords', 'consumer',
                      'available', 'total', 'original_price', 'oldprice',
                      'base_currency', 'base_price' )
  
  list_per_page = 100
  list_max_show_all = 50000
  
  def viewed_stats(self, obj):
    return obj.leadstatistics.viewed
  viewed_stats.short_description = 'viewed'
  
  def reinquire(self, obj):
    return obj.reinquire # invert the boolean value
  reinquire.boolean = False
  reinquire.admin_order_field = 'is_blocked'
  reinquire.short_description = 'Is Blocked'
  
  def moderation_to_active(self, request, queryset):
    count = 0
    for i in queryset:
      if i.active == False and i.inactive_reason == 'moderate':
          i.active = True
          i.inactive_reason = ''
          i.save()
          count = count + 1
    self.message_user(request, 
      "Lead status has been changed from moderation " + \
      "to active for %d leads" % count)
  
  def email_sent(self, instance):
    if instance.workernoticeemailtask_set.exists():
      wt = instance.workernoticeemailtask_set.latest('pk')
      return wt.workernoticematchedfilter_set.count()
    return 0

  def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=leads.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Description"),
        smart_str(u"Read_more_link"),
        smart_str(u"Image"),
        smart_str(u"Price"),
        smart_str(u"Original_price"),
        smart_str(u"Oldprice"),
        smart_str(u"Price_currency"),
        smart_str(u"Sale"),
        smart_str(u"Sold"),
        smart_str(u"Pre_sold"),
        smart_str(u"Seller"),
        smart_str(u"Reference"),
        smart_str(u"Consumer"),
        smart_str(u"Deal_starts"),
        smart_str(u"Deal_ends"),
        smart_str(u"Budget"),
        smart_str(u"Budget_currency"),
        smart_str(u"Category"),
        smart_str(u"Keywords"),
        smart_str(u"Viewed"),
        smart_str(u"Shared"),
        smart_str(u"Active"),
        smart_str(u"Status"),
        smart_str(u"Language"),
        smart_str(u"Timezone"),
        smart_str(u"Generation_method"),
        smart_str(u"Generation_source"),
        smart_str(u"Generation_date"),
        smart_str(u"Ranking"),
        smart_str(u"Created"),
        smart_str(u"Modified"),
        smart_str(u"Inactive_reason"),
        smart_str(u"Inactive_date"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.title),
            smart_str(obj.description),
            smart_str(obj.read_more_link),
            smart_str(obj.image),
            smart_str(obj.price),
            smart_str(obj.original_price),
            smart_str(obj.oldprice),
            smart_str(obj.price_currency),
            smart_str(obj.sale),
            smart_str(obj.sold),
            smart_str(obj.pre_sold),
            smart_str(obj.seller),
            smart_str(obj.reference),
            smart_str(obj.consumer),
            smart_str(obj.deal_starts),
            smart_str(obj.deal_ends),
            smart_str(obj.budget),
            smart_str(obj.budget_currency),
            smart_str(obj.category),
            smart_str(obj.keywords),
            smart_str(obj.leadstatistics.viewed),
            smart_str(obj.leadstatistics.shared),
            smart_str(obj.active),
            smart_str(obj.status),
            smart_str(obj.language),
            smart_str(obj.timezone),
            smart_str(obj.generation_method),
            smart_str(obj.generation_source),
            smart_str(obj.generation_date),
            smart_str(obj.ranking),
            smart_str(obj.created),
            smart_str(obj.modified),
            smart_str(obj.inactive_reason),
            smart_str(obj.inactive_date),
        ])
    return response
  export_csv.short_description = u"Export CSV"

class LeadStatisticsAdmin(admin.ModelAdmin):
  list_display = ('id', 'lead', 'viewed', 'shared', 'modified',)
  search_fields = ['lead__id', 'lead__title',]
  date_hierarchy = 'modified'

  def __init__(self, *args, **kwargs):
    super(LeadStatisticsAdmin, self).__init__(*args, **kwargs)
    self.list_display_links = (None,)  
  
  def get_readonly_fields(self, request, obj=None):
    return [field.name for field in self.opts.local_fields]

  def has_add_permission(self, request):
    return False

  def has_delete_permission(self, request, obj=None):
    return False

class LeadRequestAdmin(admin.ModelAdmin):
  list_display = (
      'id', 'title', 'buyer', 'location', 'leads_needed_with_unit',
      'created', 'status', 
  )
  list_filter = ['language', 'status']
  search_fields = ['id', 'title', 'description']
  date_hierarchy = 'created'
  fieldsets = [
      ('Basics',            {'fields': ['title']}),
      (None,                {'fields': ['description']}),
      (None,                {'fields': ['read_more_link']}),  
      ('Buyer',             {'fields': ['buyer'],}),
      ('Detailed information', {'fields': ['deal_starts', 'deal_ends']}),      
      (None,                {'fields': ['budget_min','budget_max', 'budget_currency']}),
      (None,                {'fields': ['price_min','price_max', 'price_currency']}),   
      (None,                {'fields': ['rank_min', 'rank_max']}),
      (None,                {'fields': ['leads_needed', 'leads_needed_unit']}),                  
      ('Classification',    {'fields': ['category']}),
      (None,                {'fields': ['keywords']}),
      ('Requested Localization', {'fields': ['location', 'geotag']}),
      (None,                {'fields': ['requested_language']}),              
      ('Statistics',        {'fields': ['viewed', 'shared']}),                              
      ('Localization',      {'fields': ['language','timezone']}),      
      ('Tacking',           {'fields': ['generation_method']}),
      #('Date information',  {'fields': ['created', 'modified']}),
      ('Status',             {'fields': ['active', 'status']}),         
  ]
  readonly_fields = ('buyer', 'keywords', )

  list_per_page = 100

  def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=requestedlead.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Description"),
        smart_str(u"Read_more_link"),
        smart_str(u"Deal_starts"),
        smart_str(u"Deal_ends"),
        smart_str(u"Budget_min"),
        smart_str(u"Budget_max"),
        smart_str(u"Budget_currency"),
        smart_str(u"Price_min"),
        smart_str(u"Price_max"),
        smart_str(u"Price_currency"),
        smart_str(u"Rank_min"),
        smart_str(u"Rank_max"),
        smart_str(u"Category"),
        smart_str(u"Keywords"),
        smart_str(u"Leads_needed"),
        smart_str(u"Leads_needed_unit"),
        smart_str(u"Viewed"),
        smart_str(u"Shared"),
        smart_str(u"Active"),
        smart_str(u"Status"),
        smart_str(u"Location"),
        smart_str(u"Geotag"),
        smart_str(u"Language"),
        smart_str(u"Timezone"),
        smart_str(u"Requested_language"),
        smart_str(u"Generation_method"),
        smart_str(u"Created"),
        smart_str(u"Modified"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.title),
            smart_str(obj.description),
            smart_str(obj.read_more_link),
            smart_str(obj.deal_starts),
            smart_str(obj.deal_ends),
            smart_str(obj.budget_min),
            smart_str(obj.budget_max),
            smart_str(obj.budget_currency),
            smart_str(obj.price_min),
            smart_str(obj.price_max),
            smart_str(obj.price_currency),
            smart_str(obj.rank_min),
            smart_str(obj.rank_max),
            smart_str(obj.category),
            smart_str(obj.keywords),
            smart_str(obj.leads_needed),
            smart_str(obj.leads_needed_unit),
            smart_str(obj.viewed),
            smart_str(obj.shared),
            smart_str(obj.active),
            smart_str(obj.status),
            smart_str(obj.location),
            smart_str(obj.geotag),
            smart_str(obj.language),
            smart_str(obj.timezone),
            smart_str(obj.requested_language),
            smart_str(obj.generation_method),
            smart_str(obj.created),
            smart_str(obj.modified),
        ])
    return response
  export_csv.short_description = u"Export CSV"
    
  actions = [export_csv]   

  def leads_needed_with_unit(self, instance):
    return instance.leads_needed + ' per ' + instance.leads_needed_unit
  leads_needed_with_unit.admin_order_field = 'leads_needed_unit'
  leads_needed_with_unit.short_description = 'leads needed'

class LeadCategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'parent_id', 'category_number', 'name')
  list_filter = ['parent', 'name']
  search_fields = ['id', 'name','lead__id','lead__title']
  
  fieldsets = [
      ('Basics', {'fields': ['id', 'parent', 'parent_id', 'category_number', 'name' ]})         
  ]
  
  readonly_fields = ('id', 'parent_id')
  
  list_per_page = 100

  def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=leadcategory.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Name"),
        smart_str(u"Parent"),
        smart_str(u"Parent_id"),
        smart_str(u"Category_number"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.name),
            smart_str(obj.parent),
            smart_str(obj.parent_id),
            smart_str(obj.category_number),
        ])
    return response
  export_csv.short_description = u"Export CSV"
    
  actions = [export_csv]   
  
  def parent_id(self, instance):
     if  instance.parent:
        return instance.parent.id
     else:
         return None

class LeadKeywordAdmin(admin.ModelAdmin):
  search_fields = ['name', 'lead__title', 'lead__id']
  ordering = ('name',)
  list_per_page = 100

  def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=leadkeywords.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Name"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.name),
        ])
    return response
  export_csv.short_description = u"Export CSV"
    
  actions = [export_csv]   

class ConsumerAddressAdmin(admin.ModelAdmin):
  list_display = (
      'id', 'street', 'city', 'postal_code','country',
  )
  list_filter = ['country']
  search_fields = ['id', 'street', 'city', 'postal_code', 'country',]

class ConsumerCompanyAdmin(admin.ModelAdmin):
  list_display = (
      'id', 'industry', 'no_of_employees', 'turn_over',
      'profit', 'visiting_address'
  )
  list_filter = ['industry', 'no_of_employees']
  search_fields = ['id', 'industry']
  readonly_fields = ('visiting_address', )

class LeadRequestedLanguageAdmin(admin.ModelAdmin):
  search_fields = ['name']

class LeadAskQuestionAdmin(admin.ModelAdmin):
  list_display = (
    'lead', 'actor', 'email', 'question','website','ipaddress','created', )
  search_fields = ['question', 'email', 
    'lead__id', 'lead__title', 'actor__id', 'actor__email','actor__username',
  ]
  date_hierarchy = 'created'
  readonly_fields = ('lead','actor','email','phone_number')
  

admin.site.register(Lead, LeadAdmin)
admin.site.register(LeadStatistics, LeadStatisticsAdmin)
admin.site.register(LeadCategory, LeadCategoryAdmin)
admin.site.register(LeadKeyword, LeadKeywordAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(ConsumerAddress, ConsumerAddressAdmin)
admin.site.register(ConsumerCompany, ConsumerCompanyAdmin)
admin.site.register(LeadRequest, LeadRequestAdmin)
admin.site.register(LeadRequestedLanguage, LeadRequestedLanguageAdmin)
admin.site.register(LeadAskQuestion,LeadAskQuestionAdmin)
