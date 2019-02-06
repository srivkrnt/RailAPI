from django.db import models

# Create your models here.
class TrainDetails(models.Model):
    trainNo = models.IntegerField()
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)

class PnrDetails(models.Model):
    pnrno = models.IntegerField()
    status = models.CharField(max_length=4)
    trainInfo = models.CharField(max_length=60)
    boardingPoint = models.CharField(max_length=40)
    destinationPoint = models.CharField(max_length=40)
    date = models.DateField()
    coachType = models.CharField(max_length=10)
