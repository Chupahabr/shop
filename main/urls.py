from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile, name="profile"),
    path('p-<str:people>/c-<slug:category>/t-<slug:type>', views.prod_type_list, name="prod_type_list"),
    path('p-<str:people>/c-<slug:category>/', views.type_prod, name="type_prod"),
    path('p-<str:people>/', views.category_list, name="category_list"),
    path('', views.index, name="main"),
]
