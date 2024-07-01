from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

def base(request):
    user = request.user
    data = {'user':user}
    return render(request,'base.html',data)



class Home(ListView):
    model = Products
    template_name = 'App_shop/home.html'
    context_object_name = 'lists'


class ProductDetail(DetailView):
    model = Products
    template_name = 'App_shop/pd.html'
    context_object_name = 'object'