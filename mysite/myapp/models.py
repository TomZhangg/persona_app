from django.db import models

# Create your models here.
class Persona(models.Model):
	name = models.CharField(max_length=120) #max length required
	persona = models.CharField(max_length=120)
	followers = models.BigIntegerField()