from django.shortcuts import render, get_object_or_404,redirect
from .models import Product, ProductImage
from .forms import ProductForm
import random

def index(request):
    return render(request, 'main/index.html', {'title': ''})

def page1(request):
    return render(request, 'main/page1.html')

def page2(request):
    products = list(Product.objects.all())
    random_products = random.sample(products, min(len(products), 8))

    for product in products:
        product.main_image = product.images.filter(is_main=True).first()

    return render(request, 'main/page2.html', {'products': products})


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
        'description': product.description
    })


from django.shortcuts import render
from .forms import ProductForm
from .models import ProductImage
import os
from django.conf import settings

def handle_uploaded_file(file, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return f'{filename}'

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

            is_main_set = False
            for i in range(1, 5):
                image_field = request.FILES.get(f'image_{i}')
                if image_field:
                    is_main = not is_main_set
                    if is_main:
                        is_main_set = True

                    image_url = handle_uploaded_file(image_field, image_field.name)

                    ProductImage.objects.create(
                        product=product,
                        image_url=image_url,
                        is_main=is_main
                    )

            return render(request, 'product/create_product.html', {
                'form': ProductForm(),
                'success_message': 'Продукт успешно создан!'
            })
    else:
        form = ProductForm()

    return render(request, 'product/create_product.html', {'form': form})
