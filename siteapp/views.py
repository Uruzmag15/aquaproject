from django.shortcuts import render, get_object_or_404
from .models import Brand, Tara, Drink

def home(request):
	brands = Brand.objects.all()
	return render(request, 'siteapp/home.html', {'brands': brands,})
	
def catalog(request):
	brands = Brand.objects.all()
	return render(request, 'siteapp/catalog.html', {'brands': brands,})
	
def brand_detail(request, pk):
	brands = Brand.objects.all()
	brand1 = get_object_or_404(Brand, pk=pk)
	taras = Tara.objects.filter(brand=brand1).order_by('volume')
	drinks = Drink.objects.filter(brand=brand1)
	return render(request, 'siteapp/brand_detail.html', {'brands': brands, 'taras': taras, 'drinks': drinks, 'brand1': brand1,})
	
def aboutus(request):
	brands = Brand.objects.all()
	return render(request, 'siteapp/aboutus.html', {'brands': brands,})
	
def partnership(request):
	brands = Brand.objects.all()
	return render(request, 'siteapp/partnership.html', {'brands': brands,})
	
def contacts(request):
	brands = Brand.objects.all()
	return render(request, 'siteapp/contacts.html', {'brands': brands,})
