# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('full_name', models.CharField(max_length=30, verbose_name='Full name')),
                ('category', models.CharField(max_length=30, verbose_name='Category')),
                ('subject', models.CharField(max_length=30, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('timestamp', models.DateTimeField(verbose_name='Date stamp', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'listener',
                'ordering': ('category', 'timestamp'),
                'verbose_name_plural': 'Listeners',
            },
        ),
    ]
