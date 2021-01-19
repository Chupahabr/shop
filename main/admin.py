from django import forms
from django.contrib import admin
from .models import category, product, production_type, brand, sport_type
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register

admin.site.register(category)
admin.site.register(production_type)
admin.site.register(brand)
admin.site.register(sport_type)
admin.site.register(product)

class categoryAdmin(TranslationAdmin):
    list_display = ('category',)
    list_display_links = ('category')