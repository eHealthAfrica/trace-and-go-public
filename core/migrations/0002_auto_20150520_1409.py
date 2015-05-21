# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
from django.conf import settings
import organizations.base


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseInvestigator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['organization', 'user'],
                'abstract': False,
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the organization', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('users', models.ManyToManyField(related_name='core_healthfacility', through='core.CaseInvestigator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HealthFacilityAdministrator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.OneToOneField(related_name='owner', to='core.HealthFacility')),
                ('organization_user', models.OneToOneField(to='core.CaseInvestigator')),
            ],
            options={
                'abstract': False,
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_code', models.CharField(default=core.models.id_generator, unique=True, max_length=20, db_index=True)),
                ('first_name', models.CharField(max_length=250, blank=True)),
                ('last_name', models.CharField(max_length=250, blank=True)),
                ('case_id', models.CharField(max_length=250, blank=True)),
                ('contact_phone_number', models.CharField(max_length=250, blank=True)),
                ('status', models.CharField(blank=True, max_length=1, choices=[(b'A', b'Just admitted'), (b'S', b'Stable'), (b'C', b'Condition not improving'), (b'G', b'Getting better'), (b'D', b'You will receive a call from the doctor'), (b'O', b'Discharged')])),
                ('line_listing', models.TextField(null=True, editable=False, blank=True)),
                ('health_facility', models.ForeignKey(to='core.HealthFacility')),
            ],
        ),
        migrations.AddField(
            model_name='caseinvestigator',
            name='organization',
            field=models.ForeignKey(related_name='organization_users', to='core.HealthFacility'),
        ),
        migrations.AddField(
            model_name='caseinvestigator',
            name='user',
            field=models.ForeignKey(related_name='core_caseinvestigator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='caseinvestigator',
            unique_together=set([('user', 'organization')]),
        ),
    ]
