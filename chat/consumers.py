import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.db.models import Q
from chat.models import Chats, Messages
from users.models import Account

class ChatConsumer(AsyncWebsocketConsumer):
    user = None
    room = None

    async def connect(self):
        room = self.scope['url_route']['kwargs']['room_name']
        current =self.scope['user']
        user_id = current.id
        room = await self.create_room(user_id,room)


        self.room_name = room
        self.room_group_name = 'chat_%s' % self.room_name

        self.user = user_id
        self.room = room

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


        await self.save_message(self.user,self.room,message)
        # Send message to room group
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
    def create_room(self,sender,reciever):

        msg_sender = Account.objects.get(id=sender)
        msg_reciever = Account.objects.get(id=reciever)

        print(msg_sender)
        print(msg_reciever)


        room_name = str(msg_sender.id)+(msg_sender.username)+str(msg_reciever.id)+(msg_reciever.username)



        if msg_sender == msg_reciever:

            pass
        else:

            try:
                
                room = Chats.objects.get(Q(sender=sender,reciever=reciever)|Q(sender=reciever,reciever=sender))  
            except:

                room = Chats.objects.create(sender_id=sender,reciever_id=reciever,room_name=room_name)   
            return room 

    @database_sync_to_async
    def save_message(self,user,room,message):

        return Messages.objects.create(user_id=user,room_id=room.id,message=message)


