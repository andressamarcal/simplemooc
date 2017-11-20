from django.conf.urls import include, url
import simplemooc.courses import Course

urlpatterns = [
    url(r'^$', 'index', name='index'),
    #url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details')
]
