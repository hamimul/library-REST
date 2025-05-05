from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .serializers import BookSerializer, AuthorSerializer
from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]