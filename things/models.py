from django.db import models
from django.core.validators import MaxValueValidator 

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
