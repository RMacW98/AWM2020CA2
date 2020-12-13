# Generated by Django 3.1.1 on 2020-12-07 14:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
