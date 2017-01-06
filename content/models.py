from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name
    def die():
        self.delete()

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    company = models.ManyToManyField(Company)
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()
    image = models.CharField(max_length=500)
    style = models.CharField(max_length=500)
    imagefile = models.ImageField(upload_to = 'uploads/')
    def get_absolute_url(self):
        return '/all_articles/{0}'.format(self.id)