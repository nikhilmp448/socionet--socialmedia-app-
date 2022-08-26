from rest_framework import permissions
from friends.models import FriendRequest
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from fgroups.models import Group_members, Groups
from fgroups.serializers import Group_memberSerializer, GroupSerializer
from users.models import Account
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q

from rest_framework import serializers

from users.serializers import UserSerializer
# Create your views here.


class groupViewSet(viewsets.ModelViewSet):
    """Groups"""
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class group_memberViewSet(viewsets.ModelViewSet):
    """Group_members"""
    queryset = Group_members.objects.all()
    serializer_class = Group_memberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer=Group_memberSerializer(data=request.data)
        friend=FriendRequest.objects.filter(request_to=self.request.data['member'],status='Accepted',owner=request.user).exists()
        group= Group_members.objects.filter(group=self.request.data['group'],member=self.request.data['member']).first()
        if serializer.is_valid():
            if group:
                raise serializers.ValidationError({"message":"member is already in group"})
            elif friend :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise serializers.ValidationError({"message":"You are not friend"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False,methods=['GET'])
    def my_groups(self,request):
        my_group= Group_members.objects.filter(Q(member=self.request.user) | Q(group__owner=self.request.user))
        group = []
        for x in my_group:
            print(x.group.group_name)
            group.append((x.group.id, x.group.group_name))

            data ={
                "groups" : group
            }
        return Response(data)

        
       

       


