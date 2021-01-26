from .models import category, product, production_type, brand, sport_type, user_basket
from django.db.models.query import EmptyQuerySet
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    return render(request, 'main/mainPage.html')

def profile(request):
    return render(request, 'account/profile.html')

def type_prod(request, people, name_category):
    cat = category.objects.filter(url=name_category)[0]
    g = us_people(people)
    types = production_type.objects.filter(Q(people=g) & Q(category=cat))
    return render(request, 'main/page_type.html',{'people': people, 'category': category, 'types': types, 'cat': cat})

def category_list(request, people):
    g = us_people(people)
    cat = category.objects.all()
    types = production_type.objects.filter(people=g)
    return render(request, 'main/page_catalog.html', {'cat': cat, "people": people, 'types': types})

def prod_type_list(request, people, category, type):
    g = ru_people(people)
    type_prod = production_type.objects.filter(Q(url__contains=type))
    prod_list = product.objects.filter(Q(production_type=type_prod[0]))
    return render(request, 'main/page_type_prod_list.html', {'prod_list': prod_list, 'type_prod': type_prod[0], 'g': g, "people": people})

def prod_info(request, people, pk):
    g = ru_people(people)
    t_g = us_people(people)
    prod = product.objects.filter(Q(id_prod=pk))
    _type = production_type.objects.filter(Q(p_type=prod[0].production_type) & Q(people=t_g))[0]
    _cat = category.objects.filter(category=_type.category)[0]
    _category = _type.category
    return render(request, 'main/page_prod_info.html', {'prod': prod[0], 'g': g, 'people': people, 'type': _type, 'category': _category, 'cat': _cat})

def search(request):
    search_value = request.GET.get('search', '')
    prod_list = product.objects.filter(Q(prod_name__contains=search_value))
    return render(request, 'main/search.html',{'prod_list': prod_list, 'search_value': search_value})

def search_prod_info(request, pk, ser_val):
    prod = product.objects.filter(Q(id_prod=pk))
    search_value = ser_val
    return render(request, 'main/page_prod_info_search.html', {'prod': prod[0], "search_value": search_value})
def basket(request):
    user_id = User.objects.get(username=request.user.username).id
    basket = user_basket.objects.filter(user=user_id)
    basket_prod = []
    arr_num = range(1, 11)
    full_price = 0
    for item in basket:
        count = item.count
        prod_name = item.product
        prod_list = product.objects.filter(Q(prod_name=prod_name))
        full_price += count * prod_list[0].price
        basket_prod.extend(prod_list)
    return render(request, 'main/basket.html', {'full': full_price, 'basket': basket, 'basket_prod': basket_prod, 'num': arr_num})
def buscket_insert(request):
    print('tut')
def basket_info(request, pk):
    prod = product.objects.filter(Q(id_prod=pk))
    return render(request, 'main/basket_info.html',{'prod':prod[0]})

def ru_people(people):
    if people == 'male':
        g = 'Мужские'
    elif people == 'female':
        g = 'Женские'
    elif people == 'child':
        g = 'Детские'
    return g

def us_people(people):
    if people == 'male':
        g = 'm'
    elif people == 'female':
        g = 'f'
    elif people == 'child':
        g = 'c'
    return g