from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from .models import Product, ProductCategory, Location
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


def main(request):
    title = "главная"
    products = Product.objects.all()[:4]
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
        }
        return render(request, "mainapp/products_list.html", content)

    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
    }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    locations = Location.objects.all()
    content = {"title": title, "locations": locations, "visit_date": datetime.now()}
    return render(request, 'mainapp/contact.html', content)
