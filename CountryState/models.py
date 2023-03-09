# from django.db import models
from djongo import models

# Create your models here.


class Countries(models.Model):
    countryID = models.AutoField(primary_key=True)
    countryName = models.CharField(max_length=200)
    countryValue = models.CharField(max_length=200)
    phone_code = models.IntegerField()
    currency = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200 )
    emoji = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.countryName


class Cities(models.Model):
    citiesID = models.AutoField(primary_key=True)
    name = models.CharField(default='',  max_length=200, )
    latitude = models.CharField(default='', max_length=200, )
    longitude = models.CharField(default='', max_length=200, )
    country = models.ForeignKey(
        Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, 
