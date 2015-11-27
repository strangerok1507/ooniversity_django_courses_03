from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<cid>\d+)/$', views.detail, name='detail'),
    
)