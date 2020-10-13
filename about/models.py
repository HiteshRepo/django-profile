from django.db import models

# Create your models here.


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class About(models.Model):
    bio = models.CharField(max_length=500)

    def __str__(self):
        return 'About'


class Project(models.Model):
    headline = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    organization = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


class Skill(models.Model):
    description = models.CharField(max_length=100)
    rate = IntegerRangeField(min_value=1, max_value=50)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
