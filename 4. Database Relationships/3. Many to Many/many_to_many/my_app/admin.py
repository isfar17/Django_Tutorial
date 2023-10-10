from django.contrib import admin

# Register your models here.
from .models import Article,Publication

admin.site.register(Article)
admin.site.register(Publication)
