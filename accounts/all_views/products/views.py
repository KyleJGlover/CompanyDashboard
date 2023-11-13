from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.models import *
from accounts.forms import ProductForm
from accounts.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products': products }
    return render(request, 'accounts/products/products.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            messages.error(request, 'Failed to create product because one with the same name exists')
            return redirect('create_product')
    else:
        form = ProductForm()
    context = {'form': form}  
    return render(request, 'accounts/products/create_form.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def updateProduct(request, pk):
    order = Product.objects.get(id=pk)
    form = ProductForm(instance=order)
    if request.method == 'POST':       
        form = ProductForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form }
    
    return render(request, 'accounts/products/update_form.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def deleteProduct(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context = { 'item': order }
    
    return render(request, 'accounts/products/delete_form.html', context)