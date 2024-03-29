from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class category(models.Model):
    id_category = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, verbose_name="Категории")
    url = models.CharField(max_length=50, verbose_name="URL", default="url")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class production_type(models.Model):
    id_prod = models.AutoField(primary_key=True)
    p_type = models.CharField(max_length=50, verbose_name="Тип")
    category = models.ForeignKey(category, on_delete=models.PROTECT, verbose_name="Категория", blank=True, null=True)
    
    arr_people = (
        ('m','Male'),
        ('f','Female'),
        )
    people = models.TextField(verbose_name="Люди", choices=arr_people, default='All')
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    image = models.ImageField(verbose_name='Изображения', upload_to="type/", blank=True, null=True)
    url = models.CharField(max_length=50, verbose_name="URL", default="url")

    def __str__(self):
        return self.p_type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50, verbose_name="Бренд")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class sport_type(models.Model):
    id_sport_type = models.AutoField(primary_key=True)
    sport_type = models.CharField(max_length=50, verbose_name="Вид спорта")

    def __str__(self):
        return self.sport_type

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'

class product(models.Model):
    id_prod = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=250, verbose_name="Название")
    info = models.TextField(verbose_name="Информация")
    about = models.TextField(verbose_name="Обо мне")
    upkeep = models.TextField(verbose_name="Уход")
    size_and_cut = models.TextField(verbose_name="Размер и крой", blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True, default=0)

    
    brand = models.ForeignKey(brand, on_delete=models.PROTECT, verbose_name="Бренд", blank=True, null=True)
    sport_type = models.ForeignKey(sport_type, on_delete=models.PROTECT, verbose_name="Вид спорта", blank=True, null=True)
    production_type = models.ForeignKey(production_type, on_delete=models.PROTECT, verbose_name="Тип продукта", blank=True, null=True)
    image = models.ImageField(verbose_name='Загрузить изображение', upload_to="prod/", blank=True, null=True)

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class product_images(models.Model):
    id_prod = models.ForeignKey(product, on_delete=models.PROTECT, verbose_name="Продукт")
    image = models.ImageField(verbose_name='Загрузить изображение', upload_to="prod_img/")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class user_basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь", default='2')
    product = models.ForeignKey(product, on_delete=models.PROTECT, verbose_name="Продукт")
    count = models.IntegerField(verbose_name='Количество', default='1')
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
    
class save_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    product = models.ForeignKey(product, on_delete=models.PROTECT, verbose_name="Продукт")

    class Meta:
        verbose_name = "Понравившиеся"
        verbose_name_plural = "Понравившиеся"

class delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    arr_method = (
        ('D','Delivery'),
        ('P','Pick-up service'),
        )
    delivery_method = models.TextField(verbose_name='Метод доставки', choices=arr_method)
    strit = models.TextField(verbose_name='Улица', blank=True, null=True)
    house = models.TextField(verbose_name='Дом', blank=True, null=True)
    housing = models.IntegerField(verbose_name='Корпус', blank=True, null=True)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, null=True)
    flat = models.IntegerField(verbose_name='Квартира', blank=True, null=True)
    entrance = models.IntegerField(verbose_name='Подъезд', blank=True, null=True)
    tel = models.TextField(verbose_name='Телефон', blank=True, null=True)
    price = models.IntegerField(verbose_name=("Цена"), default='0')
    date = models.DateTimeField(verbose_name=("Дата и время"), auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
