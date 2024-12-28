from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.page1),
    path('page_sosal', views.index),
    path('page2', views.page2),
    path('page3', views.page3),
    path('product/<str:url>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)