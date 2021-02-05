from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import Client
from .models import category, product, production_type, brand, sport_type, user_basket, save_item, delivery
from .views import full_price

User = get_user_model()

# Create your tests here.
class shopTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = category.objects.create(category='kateg', url='kategurl')
        self.production_type = production_type.objects.create(p_type='type1',category=self.category,people='m',description='asd',url='type1')
        self.product = product.objects.create(prod_name='name1',info='inof',about='about',upkeep='upkeep',price='10000',production_type=self.production_type) 
        self.user_basket = user_basket.objects.create(user=self.user,product=self.product)
    
    def test_app_to_cart(self):
        factory = RequestFactory()
        request = factory.post('')
        request.user = self.user
        full = full_price(request)
        print(full)

        

