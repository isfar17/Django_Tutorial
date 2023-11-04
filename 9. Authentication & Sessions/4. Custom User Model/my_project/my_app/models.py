from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import CustomUserManager

class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=14,unique=True)
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    
    objects=CustomUserManager()
    
    