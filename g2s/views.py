# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from g2s.forms import G2STransactionForm


@require_POST
@csrf_exempt
def save_g2s_transaction(request):
    form = G2STransactionForm(request.POST)
    if request.method == 'POST' and form.is_valid() and form.save():
        return HttpResponse("OK")
    return HttpResponseForbidden()
