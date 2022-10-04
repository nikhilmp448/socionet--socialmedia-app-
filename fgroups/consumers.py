import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import GroupMessages

class GroupConsumer(AsyncWebsocketConsumer):
    user = None
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'groupchat_%s' % self.room_name
        self.user = self.scope['user']
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('123456789')
        # Send message to room group
        await self.save_groupmessage(self.user,self.room_group_name,message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    @database_sync_to_async
    def save_groupmessage(self,user,room,message):
        print('11111111111111111111111111111111111111')
        return GroupMessages.objects.create(user=user,room=room,message=message)