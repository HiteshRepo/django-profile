from django.db import models
from django.utils.timezone import utc
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=50, default='Dummy Project')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.CharField(max_length=200)
    github = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    def summary_text(self):
        return self.summary.split('image_static')[0]

    def summary_img(self):
        if(len(self.summary.split('image_static')) > 1):
            return self.summary.split('image_static')[1].replace('=', '').strip()
        else:
            return None

    # def get_time_diff(self):
    #     if self.time_posted:
    #         now = datetime.datetime.utcnow().replace(tzinfo=utc)
    #         timediff = now - self.time_posted
    #         return timediff.total_seconds()
