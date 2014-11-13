# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Patient.alive'
        db.add_column(u'etu_patient', 'alive',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Patient.alive'
        db.delete_column(u'etu_patient', 'alive')


    models = {
        u'etu.patient': {
            'Meta': {'object_name': 'Patient'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'alive': ('django.db.models.fields.BooleanField', [], {}),
            'caregiver_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'enter_number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'geolocation': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['etu']