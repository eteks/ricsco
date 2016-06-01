from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^start/$', 'dashboard.views.start_new', name='index'),
    url(r'^providedlead/$', 'dashboard.views.providedlead', name='providedlead'),  
    url(r'^add_new_leads/', 'dashboard.views.add_new_leads', name='add_new_leads'),  
]
