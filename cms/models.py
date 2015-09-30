from django.db import models


class Page(models.Model):

    path = models.CharField(max_length=1024, null=False, blank=False, default='/page', unique=True)
    template = models.CharField(max_length=64, null=False, blank=False, default='base.html')
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.path


class Placeholder(models.Model):

    page = models.ForeignKey('Page')
    name = models.CharField(max_length=1024, null=False, blank=False, default='placeholder')
    content = models.TextField()

    def __unicode__(self):
        return self.name


class MediaFile(models.Model):

    name = models.CharField(max_length=1024, null=False, blank=False, default='Media File')
    file = models.FileField()

    def __unicode__(self):
        return self.name


