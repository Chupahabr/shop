from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import Client
from .models import category, product, production_type, brand, sport_type, user_basket, save_item, delivery
from .views import full_price, search

User = get_user_model()

# Create your tests here.
class shopTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = category.objects.create(category='kateg', url='kategurl')
        self.production_type = production_type.objects.create(p_type='type1',category=self.category,people='m',description='asd',url='type1')
        self.product  = product.objects.create(prod_name='name1',price='10000',production_type=self.production_type, image='url') 
        self.product2 = product.objects.create(prod_name='name2',price='20000',production_type=self.production_type, image='url') 
        self.user_basket = user_basket.objects.create(user=self.user,product=self.product)
        self.user_basket = user_basket.objects.create(user=self.user,product=self.product2)
    
    def test_app_to_cart(self):
        ser = 'name'
        factory = RequestFactory()
        request = factory.get('', {'search': ser})
        search_a = search(request)
        print('this -> ', search_a)
        # request.user = self.user
        # full = full_price(request)
        # print(request.POST['da'])
        # print(full)

        

