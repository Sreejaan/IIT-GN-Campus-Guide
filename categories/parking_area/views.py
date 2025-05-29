from django.shortcuts import render, get_object_or_404
from core.models import Facility

def parking_index(request):
    parkings = Facility.objects.filter(type='parking').order_by('name')
    return render(request, 'parking/index.html', {'parkings': parkings})

def parking_detail(request, parking_slug):
    parking = get_object_or_404(Facility, slug=parking_slug)
    return render(request, 'parking/detail.html', {'parking': parking})
