from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя продукта", max_length=128)
    image = models.ImageField(upload_to="products_images", blank=True)
    short_desc = models.CharField(verbose_name="краткое описание продукта", max_length=60, blank=True)
    description = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.DecimalField(verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Location(models.Model):
    city = models.CharField(verbose_name="city", max_length=64, blank=True)
    phone = models.CharField(verbose_name="phone", max_length=15, blank=True)
    email = models.CharField(verbose_name="email", max_length=128, blank=True)
    address = models.CharField(verbose_name="address", max_length=128, blank=True)

    def __str__(self):
        return f"{self.city} {self.address}"
