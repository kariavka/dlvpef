# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '0003_auto_20151218_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('full_name', models.CharField(help_text="The man's name for identification.", verbose_name='Full name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='E-mail', unique=True, max_length=30)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'subscriber',
                'verbose_name_plural': 'Subscribers',
                'ordering': ('email',),
            },
        ),
        migrations.DeleteModel(
            name='Listener',
        ),
    ]
