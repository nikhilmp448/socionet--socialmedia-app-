from rest_framework.response import Response
from rest_framework.decorators import action
from user_profile.models import UserProfile
from users.models import Account
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from friends.models import FriendRequest



class PostPagination(PageNumberPagination):
    page_size = 10
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
    
    def list(self, request):
        user=self.request.user.pk
        following = FriendRequest.objects.filter(request_from=user,status='Accepted')
        result=[user]
        for i in range(len(following.values())):
            result.append(following.values()[i]['request_to_id'])

        account=Account.objects.filter(id__in=result).values()
        for i in range(len(account.values())):
            result.append(account.values()[i]['id'])

        queryset=Post.objects.filter(owner__in= result).order_by('-post_date')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False,methods=['GET'])
    def all_posts(self,request):
        id=self.request.user.pk
        following = FriendRequest.objects.filter(request_from=id,status='Accepted')
        result=[id]
        for i in range(len(following.values())):
            result.append(following.values()[i]['request_to_id'])
        account=Account.objects.exclude(id__in=result).values()
        result.clear()
        for i in range(len(account.values())):
            result.append(account.values()[i]['id'])
        user = UserProfile.objects.filter(is_private=False,owner__in =result)
        result.clear()
        for i in range(len(user.values())):
            result.append(user.values()[i]['owner_id'])
        post=Post.objects.filter(owner__in = result)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)