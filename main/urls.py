from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/profile/basket', views.basket, name="basket"),
    path('accounts/profile/basket/info-<int:pk>', views.basket_info, name="basket_info"),

    path('p-<str:people>/', views.category_list, name="category_list"),
    path('p-<str:people>/c-<slug:name_category>/', views.type_prod, name="type_prod"),
    path('p-<str:people>/c-<slug:category>/t-<slug:type>', views.prod_type_list, name="prod_type_list"),
    path('p-<str:people>/info-<int:pk>', views.prod_info, name="prod_info"),
    
    path('search', views.search, name="search"),
    path('search/info-<int:pk>-<str:ser_val>', views.search_prod_info, name="search_prod_info"),

    path('bascket-insert', views.bascket_insert, name="bascket_insert"),
    path('bascket-delete', views.bascket_delete, name="bascket_delete"),
    path('bascket-count-update', views.basket_count_update, name="basket_count_update"),
    path('fav-ins', views.fav_ins, name="fav_ins"),
    path('make-dev', views.make_dev, name="make_dev"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]
