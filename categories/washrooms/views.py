from django.shortcuts import render
from core.models import WaterAndWashroom
# Create your views here.

def washroom_index(request):
    washrooms = WaterAndWashroom.objects.filter(facility_type='washroom')
    return render(request, 'washrooms/index.html', {'washrooms' : washrooms})