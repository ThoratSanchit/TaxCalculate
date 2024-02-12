from django.db import models

class incometax(models.Model):
    income=models.DecimalField(max_digits=10,decimal_places=2)
    age=models.IntegerField()