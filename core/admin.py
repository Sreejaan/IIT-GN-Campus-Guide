from django.contrib import admin
from .models import Building, Floor, Location, CampusCategory, Shop, Facility

admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Location)
admin.site.register(CampusCategory)
admin.site.register(Shop)
admin.site.register(Facility)
