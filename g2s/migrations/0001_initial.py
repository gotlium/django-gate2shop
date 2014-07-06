# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'G2STransaction'
        db.create_table(u'g2s_g2stransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('totalAmount', self.gf('django.db.models.fields.DecimalField')(default='0.00', max_digits=17, decimal_places=2)),
            ('TransactionID', self.gf('django.db.models.fields.BigIntegerField')()),
            ('ErrCode', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('ExErrCode', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('Error', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('AuthCode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('Reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('Token', self.gf('django.db.models.fields.TextField')()),
            ('responsechecksum', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('ppp_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('PPP_TransactionID', self.gf('django.db.models.fields.BigIntegerField')()),
            ('ReasonCode', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('advanceResponseChecksum', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cardCompany', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('merchantLocale', self.gf('django.db.models.fields.CharField')(default='en_US', max_length=5)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='USD', max_length=3)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('dynamicDescriptor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('tokenId', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('payment_method', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('requestVersion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('responseTimeStamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('productId', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('merchant_site_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('merchant_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('nameOnCard', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uniqueCC', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'g2s', ['G2STransaction'])


    def backwards(self, orm):
        # Deleting model 'G2STransaction'
        db.delete_table(u'g2s_g2stransaction')


    models = {
        u'g2s.g2stransaction': {
            'AuthCode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ErrCode': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Error': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ExErrCode': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Meta': {'object_name': 'G2STransaction'},
            'PPP_TransactionID': ('django.db.models.fields.BigIntegerField', [], {}),
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ReasonCode': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Token': ('django.db.models.fields.TextField', [], {}),
            'TransactionID': ('django.db.models.fields.BigIntegerField', [], {}),
            'advanceResponseChecksum': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cardCompany': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'dynamicDescriptor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'merchantLocale': ('django.db.models.fields.CharField', [], {'default': "'en_US'", 'max_length': '5'}),
            'merchant_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'merchant_site_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nameOnCard': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'ppp_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'productId': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'requestVersion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'responseTimeStamp': ('django.db.models.fields.DateTimeField', [], {}),
            'responsechecksum': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'tokenId': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'totalAmount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '17', 'decimal_places': '2'}),
            'uniqueCC': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        }
    }

    complete_apps = ['g2s']