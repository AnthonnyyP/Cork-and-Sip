from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class WineTasting(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    time = models.DateTimeField()


class Guest(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=70, blank=True, unique=True)
    user_phone = models.CharField(max_length=10)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Collection(models.Model):
    wine_name = models.CharField(max_length=50)


class Wine(models.Model):
    wine_name = models.CharField(max_length=50)
    wine_age = models.CharField(max_length=50)
    wine_origin = models.CharField(max_length=50)
