from django.db import models


# Create your models here.
class Word(models.Model):
    file = models.FileField(upload_to='uploads/', blank=False)
