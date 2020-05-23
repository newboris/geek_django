import random
from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from .models import Product, ProductCategory, Location
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


def get_basket(user):
    return Basket.objects.filter(user=user) if user.is_authenticated else []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


def main(request):
    title = "главная"
    products = Product.objects.all()[:4]
    content = {
        "title": title,
        "products": products,
        "media_url": settings.MEDIA_URL,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

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

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "hot_product": hot_product,
    }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    locations = Location.objects.all()
    content = {
        "title": title,
        "locations": locations,
        "visit_date": datetime.now(),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, 'mainapp/product.html', content)
