from django.shortcuts import render
from datetime import datetime
from .utils import read_json


def main(request):
    content = read_json('data.json').get('main')
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = read_json('data.json').get('products')
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = read_json('data.json').get('contact')
    content["visit_date"] = datetime.now()
    return render(request, 'mainapp/contact.html', content)
