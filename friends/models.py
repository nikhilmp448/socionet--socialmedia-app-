from django.db import models
from users.models import Account
# Create your models here.
class FriendRequest(models.Model):
    owner=models.ForeignKey(Account,on_delete=models.CASCADE,default=None,null=False,related_name='owner')
    request_from=models.ForeignKey(Account,on_delete=models.CASCADE,default=None,null=False,related_name='request_from')
    request_to=models.ForeignKey(Account,on_delete=models.CASCADE,default=None,null=False,related_name='request_to')
    status=models.CharField(max_length=50,default='pending')

