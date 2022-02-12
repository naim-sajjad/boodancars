from django.db import models
from django.utils import timezone
import datetime
from versatileimagefield.fields import VersatileImageField, PPOIField

class BdVehicle(models.Model):
    desc = models.TextField()
    amount = models.IntegerField()
    currency = models.CharField(max_length=60)
    vehicle_type = models.CharField(max_length=60)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    image = models.ManyToManyField('vehicle.Image', related_name='vehicles')

    class Meta:
        ordering = ['-created_at']

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name