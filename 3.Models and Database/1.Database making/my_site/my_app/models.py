from django.db import models

# Create your models here.
class Base(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    
