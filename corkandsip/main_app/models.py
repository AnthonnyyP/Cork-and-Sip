from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

TASTINGS = (
    ('M', 'Morning Tasting'),
    ('A', 'Afternoon Tasting'),
    ('N', 'Night Tasting'),
)


class Wine(models.Model):
    wine_name = models.CharField(max_length=50)
    wine_age = models.CharField(max_length=50)
    wine_origin = models.CharField(max_length=50)

    def __str__(self):
        return self.wine_name


class Guest(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=70, blank=True, unique=True)
    user_phone = models.CharField(max_length=10)
    wine = models.ManyToManyField(Wine)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guest_id': self.id})


class WineTasting(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField('Tasting Date')
    time = models.CharField(
        max_length=1,
        choices=TASTINGS,
        default=TASTINGS[0][0]
    )

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tasting_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Collection(models.Model):
    wine_name = models.CharField(max_length=50)

    def __str__(self):
        return self.wine_name
