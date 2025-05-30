from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def academic_index(request):
    return HttpResponse("Academic Category Home")

def academic_detail(request, slug):
    return HttpResponse(f"Details for academic location: {slug}")
