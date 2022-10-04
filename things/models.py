from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    quantity = models.IntegerField(default=0)
