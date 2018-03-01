# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('life', models.IntegerField(verbose_name='Life')),
                ('mana', models.IntegerField(verbose_name='Mana')),
                ('armor', models.IntegerField(verbose_name='Armor')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Character',
                'verbose_name_plural': 'Characters',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('initial_life', models.IntegerField(verbose_name='Initial Life')),
                ('initial_mana', models.IntegerField(verbose_name='Initial Mana')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Specialization',
                'verbose_name_plural': 'Specializations',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Specialization', verbose_name='Specialization'),
        ),
    ]
