# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='nav_role',
            field=models.CharField(help_text='Role of the navigation button - i.e., URL.', default='', verbose_name='Navigation role', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='nav_title',
            field=models.CharField(help_text='The text on the navigation button.', verbose_name='Navigation title', max_length=30),
        ),
    ]
