from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(request, 'accounts/dashboard.html')

def products(request):
    return HttpResponse('accounts/products.html')

def customer(request):
    return HttpResponse('accounts/customer.html')