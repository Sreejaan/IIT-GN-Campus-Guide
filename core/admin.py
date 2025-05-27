from django.contrib import admin
from .models import Building, Floor, Location, CampusCategory

admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Location)
admin.site.register(CampusCategory)