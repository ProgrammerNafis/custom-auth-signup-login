from django.db import models
from django.contrib.auth.models import User


class BillingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=276)
    zipcode = models.CharField(max_length=26)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.user_profile.username} billing address'
    
    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        
        for field_name in field_names:
            value = getattr(self,field_name)
            if value is None or value == '':
                return False
        return True
    class Meta:
        verbose_name_plural = 'Billing Address'