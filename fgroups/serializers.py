from rest_framework import serializers

from friends.models import FriendRequest
from friends.serializers import FriendRequestSerializer
from . models import Groups,Group_members
class GroupSerializer(serializers.ModelSerializer):
    # group = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Groups
        fields = ['id', 'group_name']

class Group_memberSerializer(serializers.ModelSerializer):
    # group_members = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Group_members
        fields = ['id','group', 'member','is_admin']