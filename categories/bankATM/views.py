from django.shortcuts import render, get_object_or_404
from core.models import Facility
# Create your views here.
def bank_index(request):
    bank = get_object_or_404(Facility, type='bank')
    return render(request, 'bank/index.html', {'bank': bank})