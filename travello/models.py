from django.db import models

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos')
    desc = models.TextField()
    Nickname = models.TextField()
    release = models.IntegerField()
    name1 = models.BooleanField(default=False)
    Nickname1 = models.BooleanField(default=False)
    desc1 = models.BooleanField(default=False)
    release1 = models.BooleanField(default=False)
    logo1 = models.BooleanField(default=False)

    