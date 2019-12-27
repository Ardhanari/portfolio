from django.db import models
# from django.utils import timezone
from datetime import datetime, timezone

# Create your models here.

class Project(models.Model):
    img = models.ImageField(upload_to='')
    name = models.CharField(max_length=254, default='', blank=False)
    linkGit = models.URLField(max_length=666, default='', blank=True)
    linkDepl = models.URLField(max_length=666, default='', blank=False)
    year = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name