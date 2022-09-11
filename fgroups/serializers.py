from rest_framework import serializers
from . models import Groups,Group_members


class Group_memberSerializer(serializers.ModelSerializer):
    member_name = serializers.ReadOnlyField(source='member.username')
    group_name = serializers.ReadOnlyField(source='group.group_name')
    member_id = serializers.ReadOnlyField(source='member.id')
    class Meta:
        model = Group_members
        fields = ['id','group_name','member_name','group','member', 'member_id','is_admin']
        extra_kwargs={'member':{'write_only':True,'required':True},'group':{'write_only':True,'required':True}}
class GroupSerializer(serializers.ModelSerializer):
    
    group_member = Group_memberSerializer(many=True,read_only=True)
    class Meta:
        model = Groups
        fields = ['id','group_name','group_member']