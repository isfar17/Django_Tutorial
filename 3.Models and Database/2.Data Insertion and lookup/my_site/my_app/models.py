from django.db import models

# Create your models here.
class Base(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    
    def __str__(self): #this function works when all() method is called,it creates view of the object
        return f"{self.first_name} {self.last_name}"