from django.db import models
# from django.utils import timezone
from datetime import datetime, timezone

# Create your models here.

class Project(models.Model):
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=100, default='', blank=False)
    linkGit = models.URLField(max_length=666, default='', blank=True)
    linkDepl = models.URLField(max_length=666, default='', blank=False)
    year = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Cv(models.Model):
    file = models.FileField(upload_to='files/')
    date = models.DateField(blank=False, null=True, auto_now=True)

    def __str__(self):
        return "{0} CV".format(self.date)