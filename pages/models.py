from django.db import models

# Create your models here.

class Description(models.Model):
    text = models.TextField(blank=False)
    img = models.ImageField(upload_to='img/intro/', null=True)