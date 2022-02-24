from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
