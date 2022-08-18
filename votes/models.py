from django.db import models
from posts.models import Post
from users.models import Account
# Create your models here.
class Vote(models.Model):
    post=models.ForeignKey(Post,related_name='votes',on_delete=models.CASCADE)
    up_vote_by = models.ForeignKey(Account,related_name='up_vote_user',on_delete=models.CASCADE,default=None,blank=True,null=True)
    down_vote_by=models.ForeignKey(Account,related_name='down_vote_user',on_delete=models.CASCADE,default=None,blank=True,null=True)
    def __str__(self):
        return self.post.content
