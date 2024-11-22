from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('store/', views.store, name='store'), 
    path('sample/',views.sample,name='sample'),
    path('services/',views.services,name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]