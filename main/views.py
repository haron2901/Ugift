from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request,'main/index.html', {'title':''})

def page1(request):
    return render(request,'main/page1.html')

def page2(request):
    products = Product.objects.all()
    return render(request, 'main/page2.html', {'products': products})

def page3(request):
    return render(request,'main/page3.html')

def product_detail(request, url):
    product = get_object_or_404(Product, url=url)  # ищем продукт по URL
    return render(request, 'main/product_detail.html', {'product': product})