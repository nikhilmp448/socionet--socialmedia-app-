from email.charset import Charset
from users.models import Account
from django.db import models


# Create your models here.
class Chats(models.Model):
    sender = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='sender',null=True,blank=True)
    reciever = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='reciecer',null=True,blank=True)
    room_name = models.CharField(max_length=220,null=True,blank=True)

    def __str__(self):
        return self.room_name


class Messages(models.Model):
    
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    room = models.ForeignKey(Chats,on_delete=models.CASCADE,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True, db_index=True,null=True,blank=True) 

    def __str__(self):

        return self.room.room_name    

