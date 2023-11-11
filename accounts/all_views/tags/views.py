from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.models import *
from accounts.forms import TagForm
from accounts.decorators import allowed_users

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def createTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            tag = form.save(commit=False)
            print(Tag.objects.filter(name=tag.name).exists())
            if  Tag.objects.filter(name=tag.name).exists():
                messages.error(request, 'Tag already exists')
                return redirect('create_tag') 
            else:
                Tag.objects.create(
                name=tag.name
                )
                return redirect('tags')      
    else:
        form = TagForm()
    context = {'form': form}  
    return render(request, 'accounts/tag_form.html', context)

# @allowed_users(allowed_roles=['admin'])
# @login_required(login_url='login')
# def updateProduct(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)
#     if request.method == 'POST':       
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
#     context = {'form': form }
    
#     return render(request, 'accounts/order_form.html', context)

# @allowed_users(allowed_roles=['admin'])
# @login_required(login_url='login')
# def deleteProduct(request, pk):
#     order = Order.objects.get(id=pk)
#     if request.method == 'POST':
#         order.delete()
#         return redirect('/')
        
#     context = { 'item': order }
    
#     return render(request, 'accounts/delete.html', context)