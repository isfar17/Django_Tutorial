from django.db import models

# Create your models here.
class Base(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return f"name: {self.name} age: {self.age}"

