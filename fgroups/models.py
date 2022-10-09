
from django.db import models
from friends.models import FriendRequest

from users.models import Account

# Create your models here.
class Groups(models.Model):
    owner=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='group_owner')
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name


class Group_members(models.Model):
    group=models.ForeignKey(Groups,on_delete=models.CASCADE,related_name='group_member')
    member = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='group')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.group.group_name


class GroupMessages(models.Model):
    
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    room = models.ForeignKey(Groups,on_delete=models.CASCADE,null=True,blank=True)
    message = models.TextField(null=True,blank=True) 

    def __str__(self):

        return self.room.group_name 

    
