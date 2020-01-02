from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Project(models.Model):
    img = models.ImageField(upload_to='img/projects/')
    name = models.CharField(max_length=100, default='', blank=False)
    desc = models.TextField(blank=False, null=True)
    linkGit = models.URLField(max_length=666, default='', blank=True)
    linkDepl = models.URLField(max_length=666, default='', blank=False)
    year = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name