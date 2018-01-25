from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """Serializer to map the blog model instance into JSON format"""

    class Meta:
        """Meta class"""
        model = Blog
        fields = ('id', 'slug', 'title', 'author', 'location',
                  'subtitle', 'summary', 'content', 'tags', 'created', 'modified')
        read_only_fields = ('slug',)
