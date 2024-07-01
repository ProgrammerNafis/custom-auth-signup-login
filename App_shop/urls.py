from django.urls import path
from .views import *

urlpatterns = [
    path('',base,name='base'),
    path('h/',Home.as_view(),name='home'),
    path('pd/<pk>',ProductDetail.as_view(),name='pd')
]