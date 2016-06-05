from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

# from djrill import DjrillAdminSite
# admin.site = DjrillAdminSite()
admin.autodiscover()

js_info_dict = {
    'packages': ('ricsco',),
}
urlpatterns = [
    url(r'^$', 'ricsco.views.home', name='home'),
    # url(r'^(i)', 'ricsco.views.home', name='home2'),
    url(r'^(?i)login/$', 'actors.views.login_view', name='login_view'),
    url(r'^(?i)signup/$', 'ricsco.views.signup_view', name='signup_view'),
    url(r'^(?i)logout/$', 'actors.views.logout_view', name='logout_view'),
    url(r'^(?i)create_user/$', 'actors.views.create_new_user', name='createNewUser'),
    url(r'^(?i)dashboard/', include('dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)leads/', include('leads.urls')),

]
