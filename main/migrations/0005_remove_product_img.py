# Generated by Django 5.1.4 on 2024-12-24 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_productimage_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]