from django.db import models

# Create your models here.

class Description(models.Model):
    text = models.TextField(blank=False)
    img = models.ImageField(upload_to='img/intro/', null=True)

class Cv(models.Model):
    file = models.FileField(upload_to='files/')
    date = models.DateTimeField(blank=False, null=True, auto_now=True)

    def __str__(self):
        formatedDate = self.date.strftime("%d.%m.%Y (%H:%M)")
        return "{0} CV".format(formatedDate)