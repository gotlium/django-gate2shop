# -*- encoding: utf-8 -*-

from django.conf import settings


def get_settings(key, default):
    return getattr(settings, key, default)


MERCHANT_ID = get_settings('G2S_MERCHANT_ID', '')
MERCHANT_SITE_ID = get_settings('G2S_MERCHANT_SITE_ID', '')
CURRENCY = get_settings('G2S_CURRENCY', '')
SECRET_KEY = get_settings('G2S_SECRET_KEY', '')
API_VERSION = get_settings('G2S_API_VERSION', '3.0.0')
LIVE_URL = get_settings(
    'G2S_LIVE_URL', 'https://secure.gate2shop.com/ppp/purchase.do')

MERCHANT_LOCALE = get_settings('G2S_MERCHANT_LOCALE', 'en_US')
MERCHANT_ENCODING = get_settings('G2S_MERCHANT_ENCODING', 'utf-8')

MERCHANT_LOCALES = [
    'en_US',
    'zh_ZN',
    'it_IT',
    'iw_IL',
    'ar_AA',
    'Es_ES',
    'ru_RU',
    'nl_NL',
    'pt_BR',
    'tr_TR',
    'lt_LT',
    'ro_RO',
    'pl_PL',
    'fr_FR',
    'bg_BG',
    'hr_HR',
    'de_DE',
    'da_DK',
    'ja_JP',
    'sr_RS',
    'sv_SE',
    'sl_SI'
]

MERCHANT_CURRENCIES = [
    'AUD'
    'CAD'
    'CHF'
    'DKK',
    'EUR',
    'GBP',
    'NOK',
    'SEK',
    'USD',
]
