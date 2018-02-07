from rest_framework import viewsets, generics
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer
from .utils import get_uniq_slug


class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations on blog model
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    @list_route(methods=['post'])
    def slug(self, request, *args, **kwargs):
        title = request.data.get('title', '')
        exclude_pk = request.data.get('exclude_pk', None)

        slug = get_uniq_slug(Blog, title, exclude_pk)
        return Response({'slug': slug})
