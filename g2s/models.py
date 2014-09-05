# -*- coding: utf-8 -*-

from hashlib import md5

from django.core.exceptions import ValidationError
from django.db import models

from g2s import defaults
from g2s import signals


class G2STransaction(models.Model):
    Status = models.CharField(max_length=10)
    totalAmount = models.DecimalField(
        max_digits=17, decimal_places=2, default='0.00')
    TransactionID = models.BigIntegerField()
    ErrCode = models.SmallIntegerField()
    ExErrCode = models.SmallIntegerField()
    Error = models.CharField(max_length=255, null=True, blank=True, default='')
    AuthCode = models.PositiveIntegerField(null=True, blank=True, default=0)
    Reason = models.CharField(max_length=255, null=True, blank=True)
    Token = models.TextField(null=True, blank=True)
    responsechecksum = models.CharField(max_length=50, db_index=True)
    ppp_status = models.CharField(max_length=10)
    PPP_TransactionID = models.BigIntegerField()
    ReasonCode = models.SmallIntegerField()
    advanceResponseChecksum = models.CharField(max_length=255)
    cardCompany = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20)

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)

    merchantLocale = models.CharField(
        max_length=5, default=defaults.MERCHANT_LOCALE)
    currency = models.CharField(
        max_length=3, default=defaults.CURRENCY)
    message = models.TextField()

    dynamicDescriptor = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=18)
    tokenId = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=256)
    requestVersion = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100)
    responseTimeStamp = models.DateTimeField()
    productId = models.PositiveIntegerField(null=True, blank=True)
    merchant_site_id = models.BigIntegerField()
    merchant_id = models.BigIntegerField()
    nameOnCard = models.CharField(max_length=100, null=True, blank=True)
    uniqueCC = models.CharField(max_length=255, null=True, blank=True)

    def _validate_response_checksum(self):
        fields = [
            defaults.SECRET_KEY, self.totalAmount, defaults.CURRENCY,
            self.responseTimeStamp.strftime('%Y-%m-%d.%H:%M:%S'),
            self.PPP_TransactionID, self.Status, self.productId or ''
        ]
        m = md5()
        m.update(''.join(map(str, fields)))
        if m.hexdigest() != self.advanceResponseChecksum:
            raise ValidationError('Error')

    def _send_signal(self):
        if self.Status == 'APPROVED':
            signals.g2s_payment_was_successful.send(sender=self)
        signals.g2s_signal.send(sender=self)

    def clean(self):
        self._validate_response_checksum()

    def save(self, *args, **kwargs):
        transaction_is_exists = self._default_manager.filter(
            TransactionID=self.TransactionID).exists()

        if not transaction_is_exists:
            super(G2STransaction, self).save(*args, **kwargs)
            return self._send_signal()
        return False

    def __unicode__(self):
        return str(self.PPP_TransactionID)
