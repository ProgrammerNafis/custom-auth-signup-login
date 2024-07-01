from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',sign_up,name='signup'),
    path('login/',log_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('change-profile/',profileChange,name='cp'),
    path('',profile,name='profile')
]