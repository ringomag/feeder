from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

class Feeder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FeederSet(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=models.SET_NULL, null=True, blank=True)
    reel = models.CharField(max_length=100)
    rod = models.CharField(max_length=100)
    line = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.reel + " " + self.rod

# method for updating after entry save data
@receiver(post_save, sender=FeederSet)
def clear_cache(sender, instance, **kwargs):
    # call cache clear here
    cache.clear()