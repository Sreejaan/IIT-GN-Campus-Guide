from django.shortcuts import render, get_object_or_404
from core.models import Facility
# Create your views here.

def sports_index(request):
    sports = Facility.objects.filter(type='sports').order_by('name')
    return render(request, 'sports/index.html', {'sports' : sports})

def sport_detail(request, sport_slug):
    sport = get_object_or_404(Facility, slug = sport_slug)
    return render(request, 'sports/detail.html', {'sport' : sport })

