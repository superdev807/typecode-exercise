import string
import random
from django.utils.text import slugify


def random_word(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))


def get_uniq_slug(model, title, exclude_pk=None):
    slug = slugify(title)
    unique_slug = slug
    queryset = model.objects.all()

    if exclude_pk:
        queryset = queryset.exclude(pk=exclude_pk)

    while queryset.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, random_word(5))

    return unique_slug
