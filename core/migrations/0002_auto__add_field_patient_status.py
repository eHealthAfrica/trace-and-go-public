# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Patient.status'
        db.add_column(u'core_patient', 'status',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Patient.status'
        db.delete_column(u'core_patient', 'status')


    models = {
        u'core.patient': {
            'Meta': {'object_name': 'Patient'},
            'caregiver_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'enter_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'etu': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'line_listing': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'moh_id': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']