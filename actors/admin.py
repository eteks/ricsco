from django.contrib import admin
from django.contrib.auth.models import User
from actors.models import (ActorRating,ActorReview,Rating,CompanyAddressManager,
	AddressAbstract,CompanyAddress,Ranking,CompanyReview,CompanyRating,CompanyAbstract,
	ActorAddressManager,AddressAbstract,ActorAddress,ActorCompanyManager,ActorCompany,Actor)
# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','is_staff')
    search_fields = ('first_name','email',)
    list_filter = ('is_staff','company')
    # readonly_fields = ('first_name','email')
    actions = ['delete_selected', 'export_csv']
  #   fieldsets = [
  #     ('Basics', {
  #         'fields': ['email', ]
  #     }),
  #        ('Name', {
  #         'fields': ['first_name', 'last_name','is_staff','company']
  #     }),
      
  # ]

admin.site.register(Actor,ActorAdmin)
admin.site.register(ActorReview)
admin.site.register(ActorRating)
# admin.site.register(Rating)
# admin.site.register(CompanyAddressManager)
# admin.site.register(AddressAbstract)
admin.site.register(CompanyAddress)
# admin.site.register(Ranking)
admin.site.register(CompanyReview)
admin.site.register(CompanyRating)
admin.site.register(CompanyAbstract)
# admin.site.register(ActorAddressManager)
admin.site.register(ActorAddress)
# admin.site.register(ActorCompanyManager)
admin.site.register(ActorCompany)


from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse
  
  
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'
  
    readonly_fields = LogEntry._meta.get_all_field_names() + \
                      ['object_link', 'action_description']
  
    list_filter = [
        'content_type',
        'action_flag'
    ]
  
    search_fields = [
        'object_repr',
        'change_message'
    ]
  
    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_description',
        'change_message',
    ]
  
    def has_add_permission(self, request):
        return False
  
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'
  
    def has_delete_permission(self, request, obj=None):
        return False
  
    def object_link(self, obj):
        if obj.action_flag == DELETION or obj.action_flag == ADDITION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model),
                        args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'
  
    def action_description(self, obj):
        action_names = {
            ADDITION: 'Addition',
            DELETION: 'Deletion',
            CHANGE: 'Change',
        }
        return action_names[obj.action_flag]
    action_description.short_description = 'Action'
  
admin.site.register(LogEntry, LogEntryAdmin)