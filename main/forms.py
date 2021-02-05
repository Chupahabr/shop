from django import forms
from .models import delivery
from django.forms import ModelForm, TextInput

class delivForm(ModelForm):
    class Meta:
        model = delivery
        fields = ['user','delivery_method','strit','house','housing','floor','flat','entrance','tel','price']

        widgets = {
            'strit': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Улица',
            }),
            'house': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Дом',
            }),
            'housing': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Корпус',
            }),
            'floor': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Этаж',
            }),
            'flat': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Квартира',
            }),
            'entrance': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Подъезд',
            }),
            'tel': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Телефон',
            }),
        }


# class deliveryForm(forms.Form):
#     strit = forms.CharField(max_length=50)
#     house = forms.CharField(max_length=5)
#     housing = forms.IntegerField(max_length=5)
#     floor = forms.IntegerField(max_length=5)
#     flat = forms.IntegerField(max_length=5)
#     entrance = forms.IntegerField(max_length=5)
#     tel = forms.CharField()