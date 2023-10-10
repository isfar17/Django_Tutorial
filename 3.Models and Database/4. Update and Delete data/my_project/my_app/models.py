from django.db import models

# Create your models here.
class People(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    birthdate=models.DateField()
    
    def __repr__(self):
        return f"{self.name} - {self.age} - {self.birthdate}"