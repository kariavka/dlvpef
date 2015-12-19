# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151219_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='nav_role',
            field=models.CharField(verbose_name='Navigation role', help_text='Role of the navigation button - i.e., URL.', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='nav_title',
            field=models.CharField(verbose_name='Navigation title', help_text='The text on the navigation button.', max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='role',
            field=models.CharField(verbose_name='Role', help_text='Page on the site.', max_length=16, default='main', unique=True, choices=[('main', 'Main page'), ('biography', 'Biography page'), ('information', 'Information page'), ('about', 'About page')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(verbose_name='Title', help_text='On the main page, this field it is the slogan.', max_length=256),
        ),
    ]
