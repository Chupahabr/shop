from django import forms
from django.contrib import admin
from .models import category, product, production_type, brand, sport_type, user_basket, save_item, delivery
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

admin.site.register(brand)
admin.site.register(sport_type)

@admin.register(delivery)
class deliveryAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_method')
    list_display_links = ('user',)
    readonly_fields = ('user',)

@admin.register(user_basket)
class user_basketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'count')
    list_display_links = ('user',)
    readonly_fields = ('user', 'product', 'count')

@admin.register(save_item)
class save_itemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_display_links = ('user',)
    readonly_fields = ('user', 'product')

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'brand', 'price', 'production_type', 'get_image')
    list_display_links = ('prod_name',)
    readonly_fields = ('get_image',)
    list_filter = ('brand','sport_type')
    search_fields = ('prod_name', 'production_type__p_type')
    save_as = True
    fieldsets = (
        ('Названия', {
            "fields": (('prod_name'), ('prod_name_ru'), ('prod_name_en'),)
        }),
        ('Информация', {
            "classes": ('wide', 'extrapretty'),
            "fields": 
            (
            ('info', 'info_ru', 'info_en'),
            ('about', 'about_ru', 'about_en'), 
            ('upkeep', 'upkeep_ru', 'upkeep_en'), 
            ('size_and_cut', 'size_and_cut_ru', 'size_and_cut_en')
            )
        }),
        (None, {
            "fields": (('brand', 'sport_type', 'production_type', 'price'),('image', 'get_image'))
        }),
    )

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
    # inlines = ['production_typeInline']

@admin.register(production_type)
class production_typeAdmin(admin.ModelAdmin):
    list_display = ('name_gen', 'category', 'people','url' ,'get_image')
    list_display_links = ('name_gen',)
    list_filter = ('category', 'people')
    readonly_fields = ('get_image',)

    def name_gen(self, obj):
        return f"{obj.p_type}, {obj.people}"

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="90" height="120">')
        else:
            return '(none)'

    get_image.allow_tags = True
    get_image.short_description = "Изображение"

# class production_typeInline(admin.TabularInline):
#     model = production_type
