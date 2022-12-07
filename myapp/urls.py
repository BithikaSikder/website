from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('customers', views.customers, name='customers'),
    path('products', views.products, name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)