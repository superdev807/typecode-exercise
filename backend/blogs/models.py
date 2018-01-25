from django.db import models


class Blog(models.Model):
    """ Blog model """
    title = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, blank=False, unique=True)
    author = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    subtitle = models.CharField(max_length=255, blank=False)
    summary = models.TextField(blank=False)
    content = models.TextField(blank=False)
    tags = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
