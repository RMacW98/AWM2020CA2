from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'world/data/clinic.json'
def load_data(apps, schema_editor):
    Clinic = apps.get_model('world', 'Clinic')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(jsonfile, encoding="utf8") as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    addr = tags.get('addr', 'no-addr')
                    phone = tags.get('phone', 'no-phone')
                    website = tags.get('website', 'no-webiste')
                    opening_hours = tags.get('opening_hours', 'no-opening_hours')
                    health_specialty = tags.get('healthcare:speciality', 'no-healthcare:speciality')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Clinic(name=name,addr=addr, phone=phone,website=website,opening_hours=opening_hours,health_specialty=health_specialty, lon=longitude, lat= latitude, location = location).save()
            except KeyError:
                pass

class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_clinic'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]