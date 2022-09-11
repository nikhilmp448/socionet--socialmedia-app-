from django.shortcuts import render
from rest_framework import viewsets
from blockUser.models import Userblock
from rest_framework import permissions
from users.serializers import BlockSerializer
from users. views import UserPagination
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserBlockViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = UserPagination
    
    def list(self, request):
        queryset = Userblock.objects.filter(block_owner=request.user)
        serializer = BlockSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = BlockSerializer(data=request.data)      
        if serializer.is_valid():
            already_blocked = Userblock.objects.filter(block_owner=request.user,blocked= request.data['blocked']).exists()
            if already_blocked:
                return Response({"message":"You already blocked this user.."})
            
            else:
                    serializer.save(block_owner=request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
