from .models import category, product, production_type, brand, sport_type
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    return render(request, 'main/mainPage.html')

def profile(request):
    return render(request, 'account/profile.html')

def people(request, people):
    cat = category.objects.all()
    return render(request, 'main/page_catalog.html', {'cat': cat})