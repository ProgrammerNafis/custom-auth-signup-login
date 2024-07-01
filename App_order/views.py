from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from App_shop.models import Products


@login_required
def addToCart(request,pk):
    item = get_object_or_404(Products,pk=pk)
    order_item = Cart.objects.get_or_create(item=item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request,'This item quantity was updated.')
            return redirect('home')
        else:
            order.orderitems.add(order_item[0])
            messages.info(request,'This item was added to your cart')
            return redirect('home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request,'This item was added to your cart.')
        return redirect('home')

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user,purchased=False)
    orders = Order.objects.filter(user=request.user,ordered=False)
    
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request,'App_order/cart.html',context={'carts':carts,'order':order})
    else:
        messages.warning(request,'You dont have any item in your cart!')
        return redirect('home')


@login_required
def remove(request,pk):
    item = get_object_or_404(Products,pk=pk)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request,'This item was removed from your cart')
            return redirect('cart')
          
        else:
            messages.warning(request,'This item is noti in your cart ')
            return redirect('home')
    else:
        messages.warning(request,'You dont have an active order')
        return redirect('home')
    
@login_required
def increase_cart(request,pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.warning(request,f'{item.name} quantity has been updated')
                return redirect('cart')

        else:
            messages.warning(request,f"{item.name} is not in your cart")
            return redirect('home')
    else:
        messages.warning(request,'You dont have an active order')
        return redirect('home')

@login_required
def decrease_cart(request,pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.warning(request,f'{item.name} quantity has been updated')
                return redirect('cart')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request,f'{item.name} has been removed from your cart')
                return redirect('cart')

        else:
            messages.warning(request,f"{item.name} is not in your cart")
            return redirect('home')

    else:
        messages.warning(request,'You dont have an active order')
        return redirect('home')
        
