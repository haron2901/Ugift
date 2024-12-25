from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage
import random

def index(request):
    return render(request, 'main/index.html', {'title': ''})

def page1(request):
    return render(request, 'main/page1.html')

def page2(request):
    products = list(Product.objects.all())

    random_products = random.sample(products, min(len(products), 8))

    category_filter = request.GET.get('category')
    if category_filter:
        random_products = [product for product in random_products if product.category == category_filter]

    who_filter = request.GET.get('who')
    if who_filter:
        random_products = [product for product in random_products if product.for_who == who_filter]

    for product in random_products:
        product.main_image = product.images.filter(is_main=True).first()  # Получаем только главное изображение

    return render(request, 'main/page2.html', {'products': random_products})


def page3(request):
    return render(request, 'main/page3.html')

def product_detail(request, url):
    product = get_object_or_404(Product, url=url)
    main_image = product.images.filter(is_main=True).first()
    images = product.images.all()
    if main_image:
        images = [main_image] + [img for img in images if img != main_image]

    return render(request, 'main/product_detail.html', {
        'product': product,
        'main_image': main_image,
        'images': images,
        'description': product.description  # Добавляем описание продукта в контекст
    })