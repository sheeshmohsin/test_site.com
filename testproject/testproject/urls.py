from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'testapp.views.home', name='home'),
    url(r'^upload/', 'testapp.views.upload'),

    url(r'^admin/', include(admin.site.urls)),
)
