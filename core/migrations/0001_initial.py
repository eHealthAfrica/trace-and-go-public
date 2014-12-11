# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'core_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, db_index=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('moh_id', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('enter_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('caregiver_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('etu', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('json', self.gf('django.db.models.fields.TextField')()),
            ('line_listing', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Patient'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'core_patient')


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
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']