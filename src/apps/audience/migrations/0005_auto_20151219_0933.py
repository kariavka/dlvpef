# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '0004_auto_20151218_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='full_name',
            field=models.CharField(help_text="The man's name for identification (not required).", blank=True, verbose_name='Full name', max_length=30),
        ),
    ]
