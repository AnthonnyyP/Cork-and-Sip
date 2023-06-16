from django.db import models

# Create your models here.


class WineTasting(models.Model):
  name = models.CharField(max_length=30)
  date = models.CharField(max_length=30)
  time = models.DateTimeField()


class Guest(models.Model):
  user_name = models.Charfield(max_length=30)
  user_email = models.EmailField(max_length=70, blank=True, unique=True)
  user_phone = models.Charfield(max_length=10)

  def __str__(self):
    return self.user_name


class Collection(models.Model):
  wine_name = models.CharField(max_length=50)

  def __str__(self):
    return self.wine_name


class Wine(models.Model):
  wine_name = models.CharField(max_length = 50)
  wine_age = models.CharField(max_length = 50)
  wine_origin = models.CharField(max_length = 50) 

  def __str__(self):
    return self.wine_name
