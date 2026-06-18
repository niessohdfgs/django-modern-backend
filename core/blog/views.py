from django.core.cache import cache
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly


# ---------------- CATEGORY ----------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------------- POST ----------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    CACHE_KEY = "posts_list"

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(self.CACHE_KEY)

        if cached_data:
            print(" CACHE HIT")
            return Response(cached_data)

        print(" CACHE MISS")

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        cache.set(self.CACHE_KEY, serializer.data, timeout=60)  # 1 minute

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        cache.delete(self.CACHE_KEY)  # invalidate cache