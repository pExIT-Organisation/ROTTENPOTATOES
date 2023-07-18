"""
URL configuration for ROTTENPOTATOES project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import concept_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pk_index', concept_views.pk_index, name='pk_index'),
    path('pk_film_ranking', concept_views.pk_film_ranking, name='pk_film_ranking'),
    path('pk_quiz', concept_views.pk_quiz, name='pk_quiz')
]
