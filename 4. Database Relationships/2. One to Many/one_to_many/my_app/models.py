from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) # foreignkey means that waiter will take the reference of
    #the restaurant, and there can be many waiters. if restaurant is deleted, then all waiters are deleted. thats what cascade means
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)