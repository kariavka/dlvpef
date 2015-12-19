# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('role', models.CharField(choices=[('main', 'Main page'), ('biography', 'Biography page'), ('information', 'Information page'), ('about', 'About page')], verbose_name='Role', unique=True, default='a', help_text='Page on the site.', max_length=16)),
                ('title', models.CharField(verbose_name='Title', help_text='On the main page, this field it is the slogan.', max_length=30)),
                ('content', models.TextField(verbose_name='Content')),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
                ('nav_title', models.CharField(verbose_name='Navigation role', help_text='Role of the navigation button - i.e., URL.', max_length=256)),
                ('nav_is_active', models.BooleanField(verbose_name='Active navigation button', default=True)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
