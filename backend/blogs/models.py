from django.db import models

from .utils import get_uniq_slug


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
        return get_uniq_slug(Blog, self.title, self.pk)

    def save(self, *args, **kwargs):
        """Override save()"""

        self.slug = self._get_unique_slug()

        super(Blog, self).save()
