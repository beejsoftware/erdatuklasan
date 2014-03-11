from django.db import models

# Create your models here.


class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)


    def __unicode__(self):
        return self.title

