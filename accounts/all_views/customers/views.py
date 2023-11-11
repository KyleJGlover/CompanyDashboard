from django.shortcuts import render, redirect

from accounts.models import *
from accounts.forms import CustomerForm

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    
    return render(request, 'accounts/customer_form.html', context)

def updateCustomer(request, pk):
    order = CustomerForm.objects.get(id=pk)
    form = CustomerForm(instance=order)
    if request.method == 'POST':       
        form = CustomerForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form }
    
    return render(request, 'accounts/customer_form.html', context)

def deleteCustomer(request, pk):
    order = CustomerForm.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context = { 'item': order }
    
    return render(request, 'accounts/delete.html', context)