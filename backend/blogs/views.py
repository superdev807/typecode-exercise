from rest_framework import viewsets

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations on blog model
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
