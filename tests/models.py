from django.db import models


class TestModel(models.Model):
    int_field = models.IntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
