from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """Serializer to map the blog model instance into JSON format"""

    class Meta:
        """Meta class"""
        model = Blog
        fields = ('id', 'slug', 'title', 'author', 'location',
                  'subtitle', 'summary', 'body', 'tags', 'created', 'modified')
