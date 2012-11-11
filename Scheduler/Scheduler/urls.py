from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^[S|s]qeduler/', include('Sqeduler.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
