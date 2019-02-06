from django.db import models

# Create your models here.
class TrainDetails(models.Model):
    trainNo = models.IntegerField()
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)
