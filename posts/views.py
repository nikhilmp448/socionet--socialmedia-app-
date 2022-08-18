
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination



class PostPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostViewSet(viewsets.ModelViewSet):
    """
    Posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
