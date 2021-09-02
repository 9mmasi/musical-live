from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField('category-new',max_length=50)

    def __str__(self): 
        return self.name


class Photo(models.Model):
    description=models.CharField(max_length=600)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)  
    image=models.ImageField(null=False,blank=False) 
    Audio=models.FileField(upload_to='media') 