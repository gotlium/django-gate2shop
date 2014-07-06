# -*- coding: utf-8 -*-
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django import forms


class ExistHiddenInput(forms.HiddenInput):
    def render(self, name, value, attrs=None):
        if value is None:
            return ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(u'<input%s />' % forms.util.flatatt(final_attrs))
