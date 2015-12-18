# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '0002_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ('category', 'timestamp'), 'verbose_name': 'message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AddField(
            model_name='listener',
            name='full_name',
            field=models.CharField(help_text="The man's name for identification.", verbose_name='Full name', blank=True, max_length=30),
        ),
    ]
