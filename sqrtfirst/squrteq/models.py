

from django.db import models

# Create your models here.
from django.db.models import FloatField


class Forsqrt(models.Model):
    first_number = models.FloatField(blank=True, null=True)
    second_number = models.FloatField(blank=True, null=True)
    third_number = models.FloatField(blank=True, null=True)
    res_1 = models.FloatField(blank=True, null=True)
    res_2 = models.FloatField(blank=True, null=True)
    unsolvable = models.CharField(max_length=50, blank=True, null=True)
