# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('deceases', models.IntegerField()),
                ('material_losses', models.IntegerField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
