from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'world/data/pharmacy.json'
def load_data(apps, schema_editor):
    Pharmacy = apps.get_model('world', 'Pharmacy')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(jsonfile, encoding="utf8") as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    addr = tags.get('addr', 'No address available')
                    phone = tags.get('phone', 'No Phone Number Available')
                    website = tags.get('website', 'No website available')
                    opening_hours = tags.get('opening_hours', 'No opening hours available')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Pharmacy(name=name,addr=addr, phone=phone,website=website,opening_hours=opening_hours, lon=longitude, lat= latitude, location = location).save()
            except KeyError:
                pass

class Migration(migrations.Migration):

    dependencies = [
        ('world', '0007_pharmacy'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]