from .models import category, product, production_type, brand, sport_type, user_basket, save_item, delivery
from django.db.models.query import EmptyQuerySet
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import delivForm
from django.shortcuts import render, redirect
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
def search(request):
    search_value = request.GET.get('search', '')
    prod_list = product.objects.filter(Q(prod_name__icontains=search_value))
    return render(request, 'main/search.html',{'prod_list': prod_list, 'search_value': search_value})
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
    return render(request, 'main/basket.html', {'full': full_price, 'basket': basket, 'basket_prod': basket_prod, 'num': arr_num, 'form': delivForm})
def make_dev(request):
    if request.method == 'POST':
        data = {
            'user': request.user.id,
            'delivery_method': request.POST['delivery_method'],
            'strit': request.POST['strit'],
            'house': request.POST['house'],
            'housing': request.POST['housing'],
            'floor': request.POST['floor'],
            'flat': request.POST['flat'],
            'entrance': request.POST['entrance'],
            'tel': request.POST['tel'],
            'price': full_price(request),
        }
        form = delivForm(data)
        if form.is_valid():
            form.save()
            form_id = delivery.objects.filter(user=request.user.id).last().id
            bask = user_basket.objects.filter(user=request.user.id)
            for item in bask:
                attr = {
                    'user_id': request.user.id,
                    'product_id': item.product,
                }

            return redirect('profile')
        else:
            error = 'Форма была не верной'
            print(error)
            return redirect('basket')
# Ajax заросы
def bascket_insert(request):
    if request.method == 'POST':
        prod_id = request.POST['bask']
        attr = {
            'user_id': request.user.id,
            'product_id': prod_id,
        }
        b_filter = user_basket.objects.filter(**attr)
        if b_filter.__len__() > 0:
            b_filter.delete()
        else:
            b = user_basket.objects.create(**attr)
            b.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")
def bascket_delete(request):
    if request.method == 'POST':
        prod_id = request.POST['prod']
        attr = {
            'user_id': request.user.id,
            'product_id': prod_id,
        }
        b_filter = user_basket.objects.filter(**attr).delete()
        fp = full_price(request)
        return HttpResponse(str(fp))
    else:
        return HttpResponse("unsuccesful")
def basket_count_update(request):
    if request.method == 'POST':
        prod_id = request.POST['prod']
        count = request.POST['count']
        attr = {
            'user_id': request.user.id,
            'product_id': prod_id,
        }
        b_prod = user_basket.objects.filter(**attr).update(count=count)
        basket = user_basket.objects.filter(user=request.user.id)
        fp = full_price(request)
        return HttpResponse(str(fp))
    else:
        return HttpResponse("unsuccesful")
def fav_ins(request):
    if request.method == 'POST':
        prod_id = request.POST['fav']
        attr = {
            'user_id': request.user.id,
            'product_id': prod_id,
        }
        b_filter = save_item.objects.filter(**attr)
        if b_filter.__len__() > 0:
            b_filter.delete()
        else:
            b = save_item.objects.create(**attr)
            b.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

# Вывод данных продукта
def basket_info(request, pk):
    prod = product.objects.filter(Q(id_prod=pk))
    attr = {
        'user_id': request.user.id,
        'product_id': pk,
    }
    b_filter = user_basket.objects.filter(**attr)
    fav = save_item.objects.filter(**attr)
    return render(request, 'main/basket_info.html',{'prod':prod[0], 'basket': b_filter, 'fav': fav})
def prod_info(request, people, pk):
    g = ru_people(people)
    t_g = us_people(people)
    prod = product.objects.filter(Q(id_prod=pk))
    _type = production_type.objects.filter(Q(p_type=prod[0].production_type) & Q(people=t_g))[0]
    _cat = category.objects.filter(category=_type.category)[0]
    _category = _type.category
    attr = {
        'user_id': request.user.id,
        'product_id': pk,
    }
    fav = save_item.objects.filter(**attr)
    b_filter = user_basket.objects.filter(**attr)
    return render(request, 'main/page_prod_info.html', {'prod': prod[0], 'fav': fav, 'g': g, 'people': people, 'type': _type, 'category': _category, 'cat': _cat, 'basket': b_filter})
def search_prod_info(request, pk, ser_val):
    prod = product.objects.filter(Q(id_prod=pk))
    search_value = ser_val
    attr = {
        'user_id': request.user.id,
        'product_id': pk,
    }
    fav = save_item.objects.filter(**attr)
    b_filter = user_basket.objects.filter(**attr)
    return render(request, 'main/page_prod_info_search.html', {'prod': prod[0], 'fav': fav, 'basket': b_filter, "search_value": search_value})


def full_price(request):
    basket = user_basket.objects.filter(user=request.user.id)
    full_price = 0
    for item in basket:
        count = item.count
        prod_name = item.product
        prod_list = product.objects.filter(Q(prod_name=prod_name))
        full_price += count * prod_list[0].price
    return full_price

# Массивы
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