from django.db import models

# Create your models here.
class SmartContract(models.Model):
    data = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
