from django.db import models
# Create your models here.
from django.db.models import CharField


class Photo(models.Model):
    name = models.CharField(max_length=100)
    creator: CharField = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '-' + self.creator
