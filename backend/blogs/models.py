from django.db import models
from django.utils.text import slugify

from .utils import random_word


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

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        queryset = Blog.objects.all()

        if self.pk:
            queryset = queryset.exclude(pk=self.pk)

        while queryset.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, random_word(5))

        return unique_slug

    def save(self, *args, **kwargs):
        """Override save()"""

        self.slug = self._get_unique_slug()

        super(Blog, self).save()
