from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_purchased = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    FOR_WHO_CHOICES = [
        ('woman', 'Девушка'),
        ('man', 'Парень'),
        ('mom', 'Мама'),
        ('dad', 'Папа'),
        ('friends', 'Друзья'),
        ('brother', 'Брат'),
        ('sister', 'Сестра'),
    ]
    for_who = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ozon_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Ozon")
    yandex_market_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Яндекс Маркет")
    wildberries_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Wildberries")

    ozon_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yandex_market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wildberries_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name} - Main: {self.is_main}"
