from django.shortcuts import render,redirect
from App_order.models import Order
from .models import *
from App_payment.forms import BillingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


import requests

import socket



@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    if not saved_address[0].is_fully_filled:
        messages.warning(request,'Plese complete your shipping address')
        return redirect('checkout')
    
    return render(request,'App_payment/payment.html',context={})
        







@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request,f'Shipping Adress saveed')
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()


    return render(request,'App_payment/checkout.html',context={'form':form,'order_items':order_items,'order_total':order_total,'saved_address':saved_address})


