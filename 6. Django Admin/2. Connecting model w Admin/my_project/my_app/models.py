from django.db import models

# Create your models here.
class Base(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __repr__(self):
        return f"{self.name} - {self.age}"

