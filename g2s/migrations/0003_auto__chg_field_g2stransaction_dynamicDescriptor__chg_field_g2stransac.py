# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'G2STransaction.dynamicDescriptor'
        db.alter_column(u'g2s_g2stransaction', 'dynamicDescriptor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'G2STransaction.requestVersion'
        db.alter_column(u'g2s_g2stransaction', 'requestVersion', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'G2STransaction.cardCompany'
        db.alter_column(u'g2s_g2stransaction', 'cardCompany', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'G2STransaction.Token'
        db.alter_column(u'g2s_g2stransaction', 'Token', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'G2STransaction.tokenId'
        db.alter_column(u'g2s_g2stransaction', 'tokenId', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'G2STransaction.nameOnCard'
        db.alter_column(u'g2s_g2stransaction', 'nameOnCard', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'G2STransaction.uniqueCC'
        db.alter_column(u'g2s_g2stransaction', 'uniqueCC', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'G2STransaction.dynamicDescriptor'
        db.alter_column(u'g2s_g2stransaction', 'dynamicDescriptor', self.gf('django.db.models.fields.CharField')(default='None', max_length=255))

        # Changing field 'G2STransaction.requestVersion'
        db.alter_column(u'g2s_g2stransaction', 'requestVersion', self.gf('django.db.models.fields.CharField')(default='3.0.0', max_length=10))

        # Changing field 'G2STransaction.cardCompany'
        db.alter_column(u'g2s_g2stransaction', 'cardCompany', self.gf('django.db.models.fields.CharField')(default='None', max_length=255))

        # Changing field 'G2STransaction.Token'
        db.alter_column(u'g2s_g2stransaction', 'Token', self.gf('django.db.models.fields.TextField')(default='None'))

        # Changing field 'G2STransaction.tokenId'
        db.alter_column(u'g2s_g2stransaction', 'tokenId', self.gf('django.db.models.fields.CharField')(default='None', max_length=255))

        # Changing field 'G2STransaction.nameOnCard'
        db.alter_column(u'g2s_g2stransaction', 'nameOnCard', self.gf('django.db.models.fields.CharField')(default='None', max_length=100))

        # Changing field 'G2STransaction.uniqueCC'
        db.alter_column(u'g2s_g2stransaction', 'uniqueCC', self.gf('django.db.models.fields.CharField')(default='None', max_length=255))

    models = {
        u'g2s.g2stransaction': {
            'AuthCode': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'ErrCode': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Error': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ExErrCode': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Meta': {'object_name': 'G2STransaction'},
            'PPP_TransactionID': ('django.db.models.fields.BigIntegerField', [], {}),
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ReasonCode': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Token': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'TransactionID': ('django.db.models.fields.BigIntegerField', [], {}),
            'advanceResponseChecksum': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cardCompany': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'dynamicDescriptor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'merchantLocale': ('django.db.models.fields.CharField', [], {'default': "'en_US'", 'max_length': '5'}),
            'merchant_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'merchant_site_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nameOnCard': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'ppp_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'productId': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'requestVersion': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'responseTimeStamp': ('django.db.models.fields.DateTimeField', [], {}),
            'responsechecksum': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'tokenId': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'totalAmount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '17', 'decimal_places': '2'}),
            'uniqueCC': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        }
    }

    complete_apps = ['g2s']