from django.shortcuts import render
from .models import CampusCategory

# Create your views here.
def core_index(request):
    categories = CampusCategory.objects.all()
    return render(request, 'core/core_index.html', {'categories' : categories})