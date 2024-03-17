from django.db import models

# Create your models here.
class Vechile(models.Model):
    plate_number = models.CharField(max_length=15, primary_key=True)
    type = models.CharField(max_length=50)
    capacity = models.PositiveBigIntegerField(default=0)