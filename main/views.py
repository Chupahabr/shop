from .models import category, product, production_type, brand, sport_type
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    return render(request, 'main/mainPage.html')

def profile(request):
    return render(request, 'account/profile.html')

def type_prod(request, people):
    print(request.headers.get('category'))
    return render(request, 'main/page_type.html')

def category_list(request, people):
    if people == 'male':
        g = 'm'
    elif people == 'female':
        g = 'f'
    elif people == 'child':
        g = 'c'
    cat = category.objects.all()
    types = production_type.objects.filter(people=g)
    print(people)
    print(cat)
    print(types)
    return render(request, 'main/page_catalog.html', {'cat': cat, "people": people, 'types': types})