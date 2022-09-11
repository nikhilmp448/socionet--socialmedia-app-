from blockUser.models import Userblock
from user_profile.serializers import ProfileSerializer
from rest_framework import serializers


from users.models import Account
class UserSerializer(serializers.ModelSerializer):
    profile_data=ProfileSerializer(read_only=True)
    class Meta:
        model = Account
        fields = ('id','username','mobile','email','is_active','password','profile_data')
        extra_kwargs={'email':{'write_only':False,'required':True},'mobile':{'write_only':False,'required':True},'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account(
                email=validated_data['email'],
                mobile=validated_data['mobile'],
                username=validated_data['username'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user

        
class BlockSerializer(serializers.ModelSerializer):
    blocked_user = serializers.ReadOnlyField(source='blocked.username')
    blocked_by = serializers.ReadOnlyField(source='block_owner.username')

    class Meta:
        model = Userblock
        fields = ('id','block_owner','blocked_by','blocked','blocked_user')
        extra_kwargs={'block_owner':{'write_only':True},'blocked':{'write_only':True,'required':True}}