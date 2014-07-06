# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import md5

from django.utils.safestring import mark_safe
from django import forms

from g2s.fields import ExistHiddenInput
from g2s.models import G2STransaction
from g2s import defaults


class G2SForm(forms.Form):
    merchant_id = forms.IntegerField(initial=defaults.MERCHANT_ID)
    merchant_site_id = forms.IntegerField(
        initial=defaults.MERCHANT_SITE_ID)
    total_amount = forms.DecimalField(max_digits=17, decimal_places=2)
    customSiteName = forms.CharField(max_length=50)
    user_token_id = forms.IntegerField()
    user_token = forms.CharField(max_length=50, initial='auto')
    productId = forms.IntegerField(required=False)

    version = forms.CharField(max_length=10, initial=defaults.API_VERSION)
    checksum = forms.CharField(max_length=50)
    time_stamp = forms.CharField()
    currency = forms.CharField(
        max_length=3, initial=defaults.CURRENCY)

    payment_method = forms.CharField(max_length=256, initial='cc_card')
    merchantLocale = forms.CharField(
        max_length=5, initial=defaults.MERCHANT_LOCALE)

    encoding = forms.CharField(
        max_length=20, initial=defaults.MERCHANT_ENCODING)
    webMasterId = forms.CharField(max_length=255, required=False)

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=40, required=False)
    email = forms.EmailField(max_length=100)
    address1 = forms.CharField(max_length=60)
    address2 = forms.CharField(max_length=60, required=False)
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=20)
    state = forms.CharField(max_length=20, required=False)
    zip = forms.CharField(max_length=18)
    phone1 = forms.CharField(max_length=18)
    phone2 = forms.CharField(max_length=18, required=False)
    phone3 = forms.CharField(max_length=18, required=False)

    def __init__(self, items_list, *args, **kwargs):
        super(G2SForm, self).__init__(*args, **kwargs)

        self.items_list = items_list
        self.initial = kwargs.get('initial')

        self.__add_items()
        self.__add_number_of_items()
        self.__add_non_exists()
        self.__set_time_stamp()
        self.__set_checksum()
        self.__hide_field()

    def __set_checksum(self):
        items = ''
        for item in self.items_list:
            items += item['item_name'] + str(
                item['item_amount']) + str(item['item_quantity'])

        m = md5()
        m.update(
            defaults.SECRET_KEY + defaults.MERCHANT_ID +
            defaults.CURRENCY + str(self.initial['total_amount']) + items +
            str(self.initial['user_token_id']) +
            self.fields['time_stamp'].initial
        )
        self.fields['checksum'].initial = m.hexdigest()

    def __set_time_stamp(self):
        self.fields['time_stamp'].initial = datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')

    def __add_non_exists(self):
        for key, val in self.initial.items():
            if key not in self.fields:
                self.fields[key] = forms.CharField(
                    initial=val, widget=ExistHiddenInput())

    def __add_number_of_items(self):
        self.fields['numberofitems'] = forms.IntegerField(
            initial=len(self.items_list))

    def __add_items(self):
        for i, item in enumerate(self.items_list, start=1):
            for key, val in item.items():
                self.fields['%s_%d' % (key, i)] = forms.CharField(initial=val)

    def __hide_field(self):
        for field in self.fields.keys():
            if self.fields.get(field):
                self.fields[field].widget = ExistHiddenInput()

    def render(self):
        return mark_safe(
            u"""
            <form action="%s" method="get">
            %s
            <input type="submit" value="Go">
            </form>""" % (self.post_action(), self.as_p())
        )

    @staticmethod
    def post_action():
        return mark_safe(defaults.LIVE_URL)


class G2STransactionForm(forms.ModelForm):
    responseTimeStamp = forms.DateTimeField(
        input_formats=['%Y-%m-%d.%H:%M:%S'])

    class Meta:
        model = G2STransaction
