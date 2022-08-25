from audioop import maxpp
from turtle import mode
from django.db import models

# Create your models here.
class Persone(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Company_name = models.CharField(max_length=200)
    Contact_number = models.CharField(max_length=13)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Password = models.CharField(max_length=15)