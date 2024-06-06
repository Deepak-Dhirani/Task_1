

from django.shortcuts import render
from .models import Repository

def repository_list(request):
    repositories = Repository.objects.all()
    return render(request, 'github_app/repository_list.html', {'repositories': repositories})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('github-connect/', views.github_connect, name='github_connect'),
    path('repositories/', views.repository_list, name='repository_list'),
]