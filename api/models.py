from django.db import models

# Create your models here.
class Translation(models.Model):
	polish = models.CharField(max_length=64)
	english = models.CharField(max_length=64)