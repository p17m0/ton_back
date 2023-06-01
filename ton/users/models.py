from django.db import models


class Account(models.Model):
    nickname = models.CharField(max_length=200)
