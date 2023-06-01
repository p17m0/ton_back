from django.db import models

# Create your models here.
class SmartContract(models.Model):
    data = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Cмарт контракт'
        verbose_name_plural = 'Смарт контракты'

    def __str__(self) -> str:
        return self.data

