from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=254, default='', blank=False)
    linkGit = models.URLField(max_length=666, default='', blank=True)
    linkDepl = models.URLField(max_length=666, default='', blank=True)
    year = timezone.now