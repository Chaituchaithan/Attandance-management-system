from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
        first_name = models.CharField(max_length = 100)
        last_name = models.CharField(max_length = 100)
        salary = models.IntegerField()
        contact = models.IntegerField()
        email = models.EmailField()
        country = models.CharField(max_length = 100)
        city = models.CharField(max_length = 100)
        address = models.CharField(max_length = 100)
