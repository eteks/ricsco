from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = [
   url(r'^leadSave/', 'leads.views.leadSave', name='leadSave'),
]
