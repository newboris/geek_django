from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
import mainapp.views as mainapp


urlpatterns = [
    path('', mainapp.main, name='main'),
    path("products/", include("mainapp.urls", namespace="products")),
    path("contact/", mainapp.contact, name="contact"),
    path('admin/', admin.site.urls),
    path("auth/", include("authapp.urls", namespace="auth")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
