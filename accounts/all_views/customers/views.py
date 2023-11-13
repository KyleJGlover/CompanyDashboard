from django.shortcuts import render, redirect

from accounts.models import *
from accounts.forms import CustomerForm
from accounts.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistartionForm
from django.contrib import messages


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createCustomer(request):
    if request.method == 'POST':
        form = UserRegistartionForm(request.POST)
        if form.is_valid():
            newCustomer = form.save()
            # Links a user with admin group when registration is performed
            Customer.objects.create(
                user=newCustomer,
                name=newCustomer.username,
                email=newCustomer.email,
                group=Customer.USER_ROLES['customer']
            )
            messages.success(request, 'Account created for ' + newCustomer.username)
            return redirect('login')
    else:
        form = UserRegistartionForm()
    
    context = {'form' : form}
    
    return render(request, 'accounts/credentials/register_customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':       
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form, 'customer' : customer}
    
    return render(request, 'accounts/customer_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteCustomer(request, pk):
    order = CustomerForm.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context = { 'item': order }
    
    return render(request, 'accounts/delete.html', context)