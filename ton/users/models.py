from django.db import models


class Account(models.Model):
    nickname = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
