from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.CharField(max_length=255)
    quantity_purchased = models.IntegerField(default=0)

    CATEGORY_CHOICES = [
        ('food', 'Еда'),
        ('gift_set', 'Подарочный набор'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='food',
    )

    FOR_WHO_CHOICES = [
        ('woman', 'Девушка'),
        ('man', 'Парень'),
        ('mom', 'Мама'),
        ('dad', 'Папа'),
    ]
    for_who = models.CharField(
        max_length=10,
        choices=FOR_WHO_CHOICES,
        default='',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ozon_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Ozon")
    yandex_market_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Яндекс Маркет")
    wildberries_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на Wildberries")

    def __str__(self):
        return self.name
