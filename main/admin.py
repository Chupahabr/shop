from django import forms
from django.contrib import admin
from .models import category, product, production_type, brand, sport_type
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register
from django.utils.safestring import mark_safe

admin.site.register(brand)
admin.site.register(sport_type)

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'get_image')
    list_display_links = ('prod_name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="90" height="120">')
        else:
            return '(none)'

    get_image.allow_tags = True
    get_image.short_description = "Изображение"

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'url')
    list_display_links = ('category',)

@admin.register(production_type)
class production_typeAdmin(admin.ModelAdmin):
    list_display = ('p_type', 'category', 'people', 'get_image')
    list_display_links = ('p_type',)
    list_filter = ('category', 'people')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="90" height="120">')
        else:
            return '(none)'

    get_image.allow_tags = True
    get_image.short_description = "Изображение"
