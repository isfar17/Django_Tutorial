from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField("Publication") #we only need to specify many_to_many in one of the tables, django will do the others


    def __str__(self):
        return self.headline