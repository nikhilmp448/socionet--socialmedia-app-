from fgroups.models import Group_members
from .models import FriendRequest
from rest_framework import serializers
from django.contrib.auth.models import User

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=FriendRequest
        fields=['request_from','request_to','status']


        def create(self, validated_data):
            user = Group_members(
                member=validated_data['member']
            )
            user.save()
            return user