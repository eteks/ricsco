from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^start/$', 'dashboard.views.start_new', name='index'),    
]
