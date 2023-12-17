from django.db import models


class RandomUser(models.Model):
    gender = models.CharField(blank=True, max_length=100)
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    street_number = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    postcode = models.CharField(blank=True, max_length=100)
    login = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    born_data = models.DateTimeField(null=True, blank=True)
    age = models.IntegerField(blank=True)
