from user_profile.models import UserProfile
from user_profile.permissions import IsOwnerOrReadOnly
from users.models import Account
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters,pagination
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import action
# Create your views here.

class UserPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UsersearchView(generics.ListAPIView):
    pagination_class = UserPagination
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']



class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    pagination_class = UserPagination
    
    def list(self, request):
        queryset = Account.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def destroy(self, request, pk) :
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response({'detail':'Account deleted successfully'},status=status.HTTP_200_OK)

    def update(self, request, pk):
        pass

    @action(detail=True,methods=['POST']) 
    def password_change(self,request,pk):
        user = request.user
        data = request.data
        if not user.check_password(data.get('old_password')):
            # raise ValidationError({"old_password": "Old password is not correct"})
            return Response({"old_password": "Old password is not correct"})
        new_password = data.get('new_password')
        new_password_confirm = data.get('new_password_confirm')
        if new_password_confirm and new_password is not None:
            if new_password == new_password_confirm:
                user.set_password(new_password)
                user.save()
                return Response({'detail':'Password changed successfully'},status=status.HTTP_200_OK)
            else:
                return Response({"detail":"Password doesn't match"})
        elif new_password is None:
            return Response({'detail':'New password field required'})
        elif new_password_confirm is None:
            return Response({'detail':'New password confirm field required'})
        # return Response({'detail':'New password confirm field required'})

        

class UserRegisterViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_profile=UserProfile(owner = user)
            user_profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        