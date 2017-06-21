# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('active', models.BooleanField()),
                ('lastActive', models.DateField()),
                ('joinDate', models.DateField(auto_now=True)),
            ],
        ),
    ]
