from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import CustomerForm
from .filters import OrderFilter
from.decorators import allowed_users, admin_only

from accounts.all_views.dashboard.views import *
from accounts.all_views.credentials.views import *
from accounts.all_views.customers.views import *
from accounts.all_views.orders.views import *
from accounts.all_views.products.views import *
from accounts.all_views.tags.views import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'total_orders' : total_orders,
               'delivered' : delivered, 'pending': pending }
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid:
            form.save()
            
    context = { 'form': form}
    return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    order_count = orders.count()  
    context = { 'customer': customer, 'orders': orders, 'order_count' : order_count, 'myFilter': myFilter }
    
    return render(request, 'accounts/customers.html', context)