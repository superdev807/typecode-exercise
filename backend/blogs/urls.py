from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BlogViewSet


router = DefaultRouter()
router.register(r'blogs', BlogViewSet, base_name='blog')

urlpatterns = [
    path('', include(router.urls)),
]
