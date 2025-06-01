from django.shortcuts import render
from core.models import WaterAndWashroom
# Create your views here.

def water_index(request):
    waters_points = WaterAndWashroom.objects.filter(facility_type='water_point')
    print(waters_points)
    return render(request, 'waters/index.html', {'water_points' : waters_points})