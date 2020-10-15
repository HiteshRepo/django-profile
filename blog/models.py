from django.db import models
from django.utils.html import strip_tags

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        my_string = self.body[:100]
        my_string = strip_tags(my_string)

        return my_string

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
