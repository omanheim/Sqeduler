from django.conf.urls import patterns, url

from Sqeduler import views

rex = r'^(?P<day>[Monday|Tuesday|Wednesday|Thursday|Friday])/$'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /Sqeduler/wednesday
    url(r'^(?P<day>[[Mm]onday|[Tt]uesday|[Ww]ednesday|[Tt]hursday|[Ff]riday|[Ss]aturday|[Ss]unday)/$', views.dayschedule, name='dayschedule'),
    # ex: /Sqeduler/CIS240/001
    url(r'^(?P<course_id>\D+\d+)/(?P<section>\d+)/(?P<id>\d+)/$', views.detail, name='detail'),

    # ex: /Sqeduler/today
    url(r'^[Tt]oday/$', views.today, name='today'),
    # ex: /Sqeduler/now
    url(r'^[Nn]ow/$', views.now, name='now'),
    # ex: /Sqeduler/whoswhere
    url(r'^[Ww]hoswhere/$', views.whoswhere, name='whoswhere'),
)


