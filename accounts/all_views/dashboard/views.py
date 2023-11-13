from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from accounts.models import *
from accounts.decorators import allowed_users, admin_only

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    # Remove admin accounts from the list of customers
    customers = Customer.objects.all().exclude(group=Customer.USER_ROLES['admin'])
    orders.order_by()
    total_customers = customers.count()
    total_orders = orders.count()
    
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers,
               'total_customers' : total_customers, 'total_orders' : total_orders,
               'delivered' : delivered, 'pending': pending }
    return render(request, 'accounts/dashboard/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tags(request):
    tags = Tag.objects.all()
    print(tags)
    context = {'tags': tags }
    return render(request, 'accounts/dashboard/tags.html', context)
