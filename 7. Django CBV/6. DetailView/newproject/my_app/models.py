from django.db import models

# Create your models here.
class Demo(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.age}"