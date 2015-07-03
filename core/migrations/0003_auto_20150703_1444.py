# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_patient_contact_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthfacility',
            options={'verbose_name_plural': 'health facilities'},
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='case_id',
            new_name='patient_id',
        ),
    ]
