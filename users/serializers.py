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
