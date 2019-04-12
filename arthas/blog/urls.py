from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'), # maps to views.home function
    path('about/', views.about, name='blog-about'), # maps to views.about function
]
