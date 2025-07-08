from django.shortcuts import render, get_object_or_404
from core.models import Building, Location



def academic_index(request):
    academic = Building.objects.filter(category='Academic')
    return render(request, 'academic/index.html', {'academic': academic})


def academic_building(request, building_slug):
    building = get_object_or_404(Building, slug=building_slug, category='Academic')
    return render(request, 'academic/building.html', {'building': building})

# def hostel_place_type(request, building_slug, place_type):
#     building = get_object_or_404(Building, slug=building_slug)
#     locations = Location.objects.filter(floor__building=building, type=place_type)
#     return render(request, 'academic/place_type.html', {
#         'building': building,
#         'locations': locations,
#         'place_type': place_type,
#     })

# def hostel_location_detail(request, building_slug, place_type, location_slug):
#     location = get_object_or_404(Location, slug=location_slug, type=place_type, floor__building__slug=building_slug)
#     return render(request, 'academic/location_detail.html', {
#         'location': location
#     })
