from django.db import models

# Create your models here.
class Person (models.Model):
  name = models.CharField(max_length=300)
  last_name = models.CharField(max_length=300)
  age = models.IntegerField()
  number = models.IntegerField(null=True, blank=True)