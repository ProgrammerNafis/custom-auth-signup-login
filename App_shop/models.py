from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    

class Products(models.Model):
    image = models.ImageField(upload_to='product-images')
    name = models.CharField(max_length=264)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    preview_text = models.CharField(max_length=924)
    detail_text = models.CharField(max_length=1000)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['-created']