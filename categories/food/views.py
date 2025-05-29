from django.shortcuts import render, get_object_or_404
from core.models import Shop

def food_index(request):
    mess = Shop.objects.filter(type='mess').order_by('name')
    canteen = Shop.objects.filter(type="food").order_by('name')
    return render(request, 'food/index.html', {'mess': mess, 'canteen': canteen})

def food_shop(request, food_slug):
    shop = get_object_or_404(Shop, slug=food_slug)
    return render(request, 'food/detail.html', {'shop': shop})
