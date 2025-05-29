from django.shortcuts import render, get_object_or_404
from core.models import Facility
# Create your views here.

def health_index(request):
    # Get the first Health Center facility
    # center = Facility.objects.filter(type='health').first()
    
    # Optional: Return 404 if no health center found
    center = get_object_or_404(Facility, type='health')
    
    return render(request, 'health_center/index.html', {'center': center})