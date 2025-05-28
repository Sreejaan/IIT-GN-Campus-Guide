from django.shortcuts import render, get_object_or_404
from core.models import Building, Location

def library_index(request):
    libraries = Building.objects.filter(category="library")
    return render(request, 'library/index.html', {'libraries': libraries})

def library_building(request, building_slug):
    building = get_object_or_404(Building, category="library", slug=building_slug)
    locations = Location.objects.filter(floor__building=building)
    return render(request, 'library/building.html', {
        'building': building,
        'locations': locations
    })
