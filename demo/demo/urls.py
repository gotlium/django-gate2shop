from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'demo.views',
    url(r'^success/', 'g2s_success', name='g2s-success'),
    url(r'^pending/', 'g2s_pending', name='g2s-pending'),
    url(r'^error/', 'g2s_error', name='g2s-error'),
    url(r'^back/', 'g2s_back', name='g2s-back'),
    url(r'^$', 'g2s_index', name='g2s-index'),
)
