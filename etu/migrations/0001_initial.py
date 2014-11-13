# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'etu_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('enter_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('caregiver_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('geolocation', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('json', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'etu', ['Patient'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'etu_patient')


    models = {
        u'etu.patient': {
            'Meta': {'object_name': 'Patient'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
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