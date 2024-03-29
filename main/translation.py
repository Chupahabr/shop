from modeltranslation.translator import TranslationOptions, register, translator
from .models import category, product, production_type, brand, sport_type

# @register(category)
# class categoryTranslationOptions(TranslationOptions):
#     fields = ('category',)

@register(category)
class categoryTranslationOptions(TranslationOptions):
    fields = ('category',)
    # empty_values = {'slug': None}
    # required_languages = ('en', 'ru')
    # required_languages = {'ru': ('category', 'Категории'), 'en': ('category', 'Category')}

@register(production_type)
class production_typeTranslationOptions(TranslationOptions):
    fields = ('p_type', 'description',)

@register(brand)
class brandTranslationOptions(TranslationOptions):
    fields = ('brand',)

@register(sport_type)
class sport_typeTranslationOptions(TranslationOptions):
    fields = ('sport_type',)

@register(product)
class productTranslationOptions(TranslationOptions):
    fields = ('prod_name', 'info', 'about', 'upkeep', 'size_and_cut',)
