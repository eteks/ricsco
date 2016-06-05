from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = [
   url(r'^leadSave/', 'leads.views.leadSave', name='leadSave'),
   url(r'^edit_leads/(?P<pk>\d+)/','leads.views.edit_leads', name='editLead'),
]
