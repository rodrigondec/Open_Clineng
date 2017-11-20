# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0003_auto_20171120_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('category', models.CharField(choices=[('PV', 'Preventiva'), ('OT', 'Outra')], default='PV', max_length=2)),
                ('date', models.DateTimeField(verbose_name='date realized')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
            ],
        ),
    ]