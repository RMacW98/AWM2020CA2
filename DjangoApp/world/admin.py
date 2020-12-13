from django.contrib.gis import admin
from .models import WorldBorder, Campsite, Clinic, Profile, Pharmacy

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Campsite, admin.OSMGeoAdmin)
admin.site.register(Clinic, admin.OSMGeoAdmin)
admin.site.register(Profile, admin.OSMGeoAdmin)
admin.site.register(Pharmacy, admin.OSMGeoAdmin)