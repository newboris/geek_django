from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp


urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),
    path("products/all", mainapp.products, name="products_all"),
    path("products/home", mainapp.products, name="products_home"),
    path("products/office", mainapp.products, name="products_office"),
    path("products/modern", mainapp.products, name="products_modern"),
    path("products/classic", mainapp.products, name="products_classic"),
    path('admin/', admin.site.urls),
]
