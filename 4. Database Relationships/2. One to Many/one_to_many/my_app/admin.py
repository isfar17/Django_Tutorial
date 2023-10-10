from django.contrib import admin

# Register your models here.
from .models import Restaurant, Waiter

admin.site.register(Restaurant)
admin.site.register(Waiter)