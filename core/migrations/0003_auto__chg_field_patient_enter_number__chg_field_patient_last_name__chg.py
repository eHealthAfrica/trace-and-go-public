# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Patient.enter_number'
        db.alter_column(u'core_patient', 'enter_number', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Patient.last_name'
        db.alter_column(u'core_patient', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Patient.first_name'
        db.alter_column(u'core_patient', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Patient.moh_id'
        db.alter_column(u'core_patient', 'moh_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Patient.caregiver_number'
        db.alter_column(u'core_patient', 'caregiver_number', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Patient.enter_number'
        raise RuntimeError("Cannot reverse this migration. 'Patient.enter_number' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Patient.enter_number'
        db.alter_column(u'core_patient', 'enter_number', self.gf('django.db.models.fields.CharField')(max_length=250))

        # User chose to not deal with backwards NULL issues for 'Patient.last_name'
        raise RuntimeError("Cannot reverse this migration. 'Patient.last_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Patient.last_name'
        db.alter_column(u'core_patient', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=250))

        # User chose to not deal with backwards NULL issues for 'Patient.first_name'
        raise RuntimeError("Cannot reverse this migration. 'Patient.first_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Patient.first_name'
        db.alter_column(u'core_patient', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=250))

        # User chose to not deal with backwards NULL issues for 'Patient.moh_id'
        raise RuntimeError("Cannot reverse this migration. 'Patient.moh_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Patient.moh_id'
        db.alter_column(u'core_patient', 'moh_id', self.gf('django.db.models.fields.CharField')(max_length=250))

        # User chose to not deal with backwards NULL issues for 'Patient.caregiver_number'
        raise RuntimeError("Cannot reverse this migration. 'Patient.caregiver_number' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Patient.caregiver_number'
        db.alter_column(u'core_patient', 'caregiver_number', self.gf('django.db.models.fields.CharField')(max_length=250))

    models = {
        u'core.patient': {
            'Meta': {'object_name': 'Patient'},
            'caregiver_number': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'enter_number': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'etu': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'line_listing': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'moh_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['core']