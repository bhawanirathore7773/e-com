from django.urls import path
from . import views

app_name = 'corporate'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.blog_list, name='blog_list'),
    path('news/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
