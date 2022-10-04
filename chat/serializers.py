from rest_framework import serializers
from .models import Chats,Messages

class MessageSerialzer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = Messages
        fields = ['id','user','user_id','message','time']