from django.db import models
class register(models.Model):
    name=models.CharField(max_length=10)
    place=models.CharField(max_length=10)
    age=models.IntegerField()
    photo=models.ImageField(upload_to='media/',null=True,blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=10)
class gallery(models.Model):
   Brand=models.CharField(max_length=10)
   Name=models.CharField(max_length=10)
   Photo=models.ImageField(upload_to='media/',null=True,blank=True)
   Price=models.IntegerField()


