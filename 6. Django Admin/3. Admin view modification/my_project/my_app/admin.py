from django.contrib import admin
from .models import Base
# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    # fields=["age","name"] #can only specify only 1 , either fields or fieldsets
    
    fieldsets=[
        ("Time Information",{"fields":['age']}),
        ("Name Information",{"fields":['name']})
    ]

admin.site.register(Base,BaseAdmin)