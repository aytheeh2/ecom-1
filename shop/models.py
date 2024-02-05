from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='Category/Images')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='Products/Images')
    desc=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField()
    stock=models.IntegerField()

    def __str__(self):
        return self.name