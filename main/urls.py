from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/profile/basket', views.basket, name="basket"),
    path('accounts/profile/basket/info-<int:pk>', views.basket_info, name="basket_info"),
    path('', views.index, name="main"),
    path('p-<str:people>/', views.category_list, name="category_list"),
    path('p-<str:people>/c-<slug:name_category>/', views.type_prod, name="type_prod"),
    path('p-<str:people>/c-<slug:category>/t-<slug:type>', views.prod_type_list, name="prod_type_list"),
    path('p-<str:people>/info-<int:pk>', views.prod_info, name="prod_info"),
    path('search', views.search, name="search"),
    path('search/info-<int:pk>-<str:ser_val>', views.search_prod_info, name="search_prod_info"),
    path('buscket-insert', views.buscket_insert, name="buscket_insert"),
    path('bascket-count-update', views.basket_count_update, name="basket_count_update"),
    path('fav-ins', views.fav_ins, name="fav_ins"),
]
