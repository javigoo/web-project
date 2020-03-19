from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    views = models.IntegerField(default=0)

class Song(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')