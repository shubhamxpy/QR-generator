from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate-qr/', views.generate_qr, name='generate_qr'),
    path('shorten-url/', views.shorten_url, name='shorten_url'),
]
