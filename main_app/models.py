from django.db import models

# Create your models here.
class Chip(models.Model):
  brand = models.CharField(max_length=100)
  flavor = models.CharField(max_length=100)
  style = models.TextField(max_length=250)
  origin = models.CharField(max_length=100)