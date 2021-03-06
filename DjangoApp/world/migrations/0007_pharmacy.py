# Generated by Django 3.1.1 on 2020-12-13 11:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_auto_20201212_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('addr', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
                ('opening_hours', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
