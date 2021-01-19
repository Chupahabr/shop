from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile, name="profile"),
    path('<str:people>/<str:category>', views.people, name="people"),
    path('<str:people>', views.people, name="people"),
    path('', views.index, name="main"),
]
