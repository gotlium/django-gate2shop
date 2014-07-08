# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseForbidden
from g2s.forms import G2STransactionForm


def save_g2s_transaction(request):
    try:
        form = G2STransactionForm(request.GET)
        if form.is_valid() and form.save():
            return HttpResponse("OK")
    except Exception, msg:
        print '[g2s]', msg.__str__()
    return HttpResponseForbidden()
