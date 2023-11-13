from django.http import HttpResponse
from django.shortcuts import redirect
from accounts.models import *

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

#multiple users can be allowed in some pages
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = request.user.customer.group
            print(allowed_roles)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Unauthorized access denied.")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = request.user.customer.group
        
        if group is None:
            redirect('login')                
        if group == 'customer':
            return redirect('user_page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            redirect('logout')
            return HttpResponse("Unauthorized access denied.")
        
    return wrapper_func