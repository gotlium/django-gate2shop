from django.forms.models import model_to_dict
from g2s.signals import g2s_signal
from pprint import pprint


def transaction_result(sender, **kwargs):
    if sender.Status == 'APPROVED':
        pprint(model_to_dict(sender))


g2s_signal.connect(
    transaction_result, dispatch_uid="demo.models.transaction_result")
