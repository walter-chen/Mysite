# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_name', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Indent',
            fields=[
                ('indent_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('indent_status', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Client')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.District')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('maintenance_id', models.CharField(max_length=50)),
                ('alarm_details', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('construction_type', models.CharField(max_length=200)),
                ('tower_type', models.CharField(blank=True, max_length=200)),
                ('room_type', models.CharField(blank=True, max_length=200)),
                ('investment_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.District')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('contract_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('contract_type', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.District')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('resource_name', models.CharField(max_length=300)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.District')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=300)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('address', models.CharField(max_length=300)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.District')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='station_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Station'),
        ),
        migrations.AddField(
            model_name='property',
            name='station_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Station'),
        ),
        migrations.AddField(
            model_name='project',
            name='station_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Station'),
        ),
        migrations.AddField(
            model_name='order',
            name='station_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Station'),
        ),
        migrations.AddField(
            model_name='indent',
            name='station_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Station'),
        ),
    ]
