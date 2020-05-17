from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from .models import Product, ProductCategory, Location


def main(request):
    title = "главная"
    products = Product.objects.all()
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    locations = Location.objects.all()
    content = {"title": title, "locations": locations, "visit_date": datetime.now()}
    return render(request, 'mainapp/contact.html', content)
