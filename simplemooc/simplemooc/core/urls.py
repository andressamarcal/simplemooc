from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
]
