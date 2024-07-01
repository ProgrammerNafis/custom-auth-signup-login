from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = UserProfile
        fields = ['username','first_name','last_name','address_1','city','zipcode','country']