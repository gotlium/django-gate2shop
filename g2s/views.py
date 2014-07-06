# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseForbidden
from g2s.forms import G2STransactionForm


def save_g2s_transaction(request):
    form = G2STransactionForm(request.GET)
    if form.is_valid() and form.save():
        return HttpResponse("OK")
    return HttpResponseForbidden()
