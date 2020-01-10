from django.db import models

# Create your models here.

class Think_Analytics(models.Model):
	name     = models.CharField(max_length=50, unique=False)
	age      = models.IntegerField(null= True, blank=True, unique=False)
	gender   = models.CharField(max_length=10, unique=False)
	Address  = models.TextField(unique=False, blank=True)
	email    = models.EmailField(unique=False, blank=True)
	image    = models.ImageField(upload_to='media', unique=False, blank=True)
	

