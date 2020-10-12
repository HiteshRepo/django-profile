from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=50, default='Dummy Project')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.CharField(max_length=200)
