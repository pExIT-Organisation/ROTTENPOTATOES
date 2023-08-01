from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('movie1/', views.movie1, name="movie1"),
]
