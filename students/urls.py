from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<sid>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^remove/(?P<sid>\d+)/$', views.remove, name='remove'),
    url(r'^edit/(?P<sid>\d+)/$', views.edit, name='edit'),
)