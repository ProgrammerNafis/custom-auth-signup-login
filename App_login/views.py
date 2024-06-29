from django.shortcuts import render,HttpResponse,HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
             messages.warning(request,'Confirm Password is not matched!')
        else:
            user = User.objects.create_user(username,email,password1)
            user.save()
            return redirect('login')
        
    return render(request,'App_login/signup.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.warning(request,'User Is not found')
        
    return render(request,'App_login/login.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('login')
