from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

from accounts.models import *
from accounts.forms import UserRegistartionForm, LoginForm

from accounts.decorators import unauthenticated_user

@unauthenticated_user
def registrationPage(request): 
    if request.method == 'POST':
        form = UserRegistartionForm(request.POST)
        if form.is_valid():
            newCustomer = form.save()
            # Links a user with admin group when registration is performed
            Customer.objects.create(
                user=newCustomer,
                name=newCustomer.username,
                email=newCustomer.email,
                group=Customer.USER_ROLES['admin']
            )
            messages.success(request, 'Account created for ' + newCustomer.username)
            return redirect('login')
    else:
        form = UserRegistartionForm()
    
    context = {'form' : form}
    return render(request, 'accounts/credentials/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    else:
        form = LoginForm()
            
    context = {'form' : form}
    return render(request, 'accounts/credentials/login.html', context)

def logoutUser(request):    
    logout(request)
    return redirect('login')