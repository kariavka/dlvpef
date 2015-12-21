# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151219_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Page title', max_length=140)),
                ('feedback_title', models.CharField(verbose_name='Feedback title', blank=True, max_length=140)),
                ('feedback_content', models.TextField(verbose_name='Feedback content', blank=True)),
                ('feedback_is_active', models.BooleanField(verbose_name='Active feddback', default=True, help_text='Uncheck to hide feedback form.')),
                ('seo_title', models.CharField(verbose_name='Title', blank=True, max_length=140, help_text='Field is used for SEO.')),
                ('seo_keywords', models.CharField(verbose_name='Keywords', blank=True, max_length=300, help_text='Field is used for SEO. Words separated by commas.')),
                ('seo_description', models.TextField(verbose_name='Brief description', blank=True, help_text='Description used for the CEO. <br/> Text can be part of the article and place no more than 200 characters on average.')),
            ],
            options={
                'verbose_name': 'information',
                'ordering': ('id',),
                'verbose_name_plural': 'Informations',
            },
        ),
    ]
