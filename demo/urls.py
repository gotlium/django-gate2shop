from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^g2s/', include('g2s.urls')),
    url(r'^g2s/', include('demo.urls')),
)
