from django.conf.urls import patterns, url

urlpatterns = patterns(
    url(r'^start/$', 'views.start_new', name='index'),    
)
