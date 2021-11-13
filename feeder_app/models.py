from django.db import models
from django.db.models.deletion import SET_NULL

class Feeder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FeederSet(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=SET_NULL, null=True, blank=True)
    reel = models.CharField(max_length=100)
    rod = models.CharField(max_length=100)
    line = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.reel + " " + self.rod
