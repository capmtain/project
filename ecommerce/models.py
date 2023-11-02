from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Fruit(models.Model):
    price=models.IntegerField()
    name=models.CharField(max_length=100)
    des=models.CharField(max_length=1000,null=True)
    char=models.CharField(max_length=100,null=True,)
    
   


    def __str__(self):
        return self.name
    

class category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class properties(models.Model):
    addr=models.TextField(null=True)
    image=models.ImageField(upload_to='imgs',null=True)
    image1=models.ImageField(upload_to='imgs',null=True)
    image2=models.ImageField(upload_to='imgs',null=True)
    des=models.TextField()
    price=models.FloatField()
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    detail=models.TextField( null=True)
   
    def __str__(self):
        return self.addr
    
class cars(models.Model):
    image=models.ImageField(upload_to='imgs',null=True)
    image1=models.ImageField(upload_to='imgs',null=True)
    image2=models.ImageField(upload_to='imgs',null=True)
    price=models.FloatField()
    des=models.TextField()
    name=models.TextField(null=True)
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    detail=models.CharField(max_length=1000,null=True)
    
  
    def __str__(self):
        return self.name
    
    
    
class mobile(models.Model):
    image=models.ImageField(upload_to='imgs',null=True)
    image1=models.ImageField(upload_to='imgs',null=True)
    image2=models.ImageField(upload_to='imgs',null=True)
    price=models.FloatField()
    des=models.TextField()
    name=models.TextField(null=True)
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    detail=models.CharField(max_length=1000,null=True)    
   
    def __str__(self):
        return self.name


    
class bikes(models.Model):
    image=models.ImageField(upload_to='imgs',null=True)
    image1=models.ImageField(upload_to='imgs',null=True)
    image2=models.ImageField(upload_to='imgs',null=True)
    price=models.FloatField()
    des=models.TextField()
    name=models.TextField(null=True)
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    detail=models.CharField(max_length=1000,null=True)

    
   
    def __str__(self):
        return self.name

class Electronics(models.Model):
    image=models.ImageField(upload_to='imgs',null=True)
    image1=models.ImageField(upload_to='imgs',null=True)
    image2=models.ImageField(upload_to='imgs',null=True)
    price=models.FloatField()
    des=models.TextField()
    name=models.TextField(null=True)
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    detail=models.TextField( null=True)
    

    
   
    def __str__(self):
        return self.name

class Furniture(models.Model):
    image=models.ImageField(upload_to='imgs',null=True)
    image1=models.ImageField(upload_to='imgs',null=True)
    image2=models.ImageField(upload_to='imgs',null=True)
    price=models.FloatField()
    des=models.TextField()
    name=models.TextField(null=True)
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    detail=models.TextField( null=True)

    
   
    def __str__(self):
        return self.name
      
    
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    contact=models.IntegerField(null=True)
    email=models.EmailField()
    
    def __str__(self):
        return self.user.username
    
    
    
    
    
    