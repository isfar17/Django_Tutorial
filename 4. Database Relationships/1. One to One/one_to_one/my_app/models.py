from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.address} the place"


class Restaurant(models.Model):
    place = models.OneToOneField("Place",on_delete=models.CASCADE,primary_key=True) #one to one field creates relation
    #on delete cascade means, if the place object is deleted, the restaurant is also deleted, we can also set it to Null,which
    #means place will not stay but restaurant will be available
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name #the name field of the Place class

