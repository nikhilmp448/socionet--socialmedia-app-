from django.db import models

from users.models import Account

# Create your models here.
class Userblock(models.Model):
    block_owner = models.ForeignKey(Account, on_delete=models.CASCADE,default=None,null=False,related_name='block_owner')
    blocked = models.ForeignKey(Account, related_name='blocked',on_delete=models.CASCADE)
    blocked_date=models.DateField(auto_now_add=True)