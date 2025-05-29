from django.shortcuts import render, get_object_or_404
from core.models import Shop
# Create your views here.

def shop_index(request):
    shops = Shop.objects.exclude(type__in=['mess', 'food']).order_by('name')
    return render(request, 'shop/index.html', {'shops' : shops})

def shop_detail(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    return render(request, 'shop/detail.html', {'shop' : shop})
