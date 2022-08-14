from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(blank = True, null = True)
    phone = models.CharField(max_length = 10)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.TimeField()
    dropoff_time = models.TimeField()
    pickup_add = models.TextField()
    dropoff_add = models.TextField()

class UserRegister(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)