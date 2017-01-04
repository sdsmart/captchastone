# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-02 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captcha', 'data_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=256)),
            ],
        ),
    ]
