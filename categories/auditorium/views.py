from django.shortcuts import render, get_object_or_404
from core.models import Facility
# Create your views here.
def auditorium_index(request):
    auditoriums = Facility.objects.filter(type="auditorium").order_by('name')
    return render(request, 'auditorium/index.html', {'auditoriums' : auditoriums})

def auditorium_detail(request, auditorium_slug):
    auditorium = get_object_or_404(Facility, slug=auditorium_slug)
    return render(request, 'auditorium/detail.html', {'auditorium': auditorium})