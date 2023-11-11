from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Customer, Product, Tag

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = ('customer', 'product', 'status')
        
class LoginForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('username', 'password')
        
class CustomerForm(forms.ModelForm):
    class Meta: 
        model = Customer
        fields = '__all__'
        exclude = ['user']
             
class UserRegistartionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'