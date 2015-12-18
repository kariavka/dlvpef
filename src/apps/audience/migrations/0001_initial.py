# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.EmailField(unique=True, max_length=30, verbose_name='E-mail')),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
            ],
            options={
                'ordering': ('email',),
                'verbose_name_plural': 'Listeners',
                'verbose_name': 'listener',
            },
        ),
    ]
