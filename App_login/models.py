from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username = models.CharField(max_length=264,blank=True)
    full_name = models.CharField(max_length=264,blank=True)
    address_1 = models.TextField(max_length=300,blank=True)
    city = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=12,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + "'s Profile"