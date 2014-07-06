from django.conf.urls import patterns, url

urlpatterns = patterns(
    'g2s.views',
    url(r'^status/$', 'save_g2s_transaction', name="g2s-success"),
)
