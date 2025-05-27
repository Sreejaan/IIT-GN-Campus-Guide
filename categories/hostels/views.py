from django.shortcuts import render, get_object_or_404
from core.models import Building, Location

def hostel_index(request):
    hostels = Building.objects.filter(category='hostel')
    return render(request, 'hostel/index.html', {'hostels': hostels})

def hostel_building(request, building_slug):
    building = get_object_or_404(Building, slug=building_slug, category='hostel')
    types = Location.TYPE_CHOICES
    return render(request, 'hostel/building.html', {'building': building, 'types': types})

def hostel_place_type(request, building_slug, place_type):
    building = get_object_or_404(Building, slug=building_slug)
    locations = Location.objects.filter(floor__building=building, type=place_type)
    return render(request, 'hostel/place_type.html', {
        'building': building,
        'locations': locations,
        'place_type': place_type,
    })

def hostel_location_detail(request, building_slug, place_type, location_slug):
    location = get_object_or_404(Location, slug=location_slug, type=place_type, floor__building__slug=building_slug)
    return render(request, 'hostel/location_detail.html', {
        'location': location
    })
