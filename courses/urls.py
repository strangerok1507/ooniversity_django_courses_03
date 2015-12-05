from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<cid>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^remove/(?P<cid>\d+)/$', views.remove, name='remove'),
    url(r'^edit/(?P<cid>\d+)/$', views.edit, name='edit'),
    url(r'^(?P<cid>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    
)