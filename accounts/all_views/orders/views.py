from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib.auth.decorators import login_required

from accounts.models import *
from accounts.forms import OrderForm
from accounts.decorators import allowed_users

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial ={'customer': customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        
    context = {'formset': formset}
    
    return render(request, 'accounts/order_form.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':       
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form }
    
    return render(request, 'accounts/order_form.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context = { 'item': order }
    
    return render(request, 'accounts/delete.html', context)