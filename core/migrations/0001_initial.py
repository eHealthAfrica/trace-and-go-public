# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseInvestigator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'name', editable=False, max_length=250, blank=True, help_text='The name in all lowercase, suitable for URL identification', unique=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_code', models.CharField(default=core.models.id_generator, unique=True, max_length=20, db_index=True)),
                ('first_name', models.CharField(max_length=250, blank=True)),
                ('last_name', models.CharField(max_length=250, blank=True)),
                ('case_id', models.CharField(max_length=250, blank=True)),
                ('status', models.CharField(blank=True, max_length=1, choices=[(b'A', b'Just admitted'), (b'S', b'Stable'), (b'C', b'Condition not improving'), (b'G', b'Getting better'), (b'D', b'You will receive a call from the doctor'), (b'O', b'Discharged')])),
                ('line_listing', models.TextField(null=True, editable=False, blank=True)),
                ('health_facility', models.ForeignKey(to='core.HealthFacility')),
            ],
        ),
        migrations.AddField(
            model_name='caseinvestigator',
            name='health_facility',
            field=models.ForeignKey(to='core.HealthFacility'),
        ),
        migrations.AddField(
            model_name='caseinvestigator',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
