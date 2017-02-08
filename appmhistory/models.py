from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Patient(models.Model):
 name = models.CharField(max_length=100)
 register_date = models.DateField()
 ci = models.CharField(max_length=15,primary_key=True)
