from django.db import models
# Create your models here.
from users.models import Account
class Post(models.Model):
    owner = models.ForeignKey(Account, related_name='posts', on_delete=models.CASCADE)
    content=models.CharField(max_length=4000)
    post_media=models.FileField(upload_to="post_media",null=True,blank=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=3000,default=None,blank=True,null=True)
    def __str__(self):
        return self.content

class Story(models.Model):
    owner = models.ForeignKey(Account, related_name='story', on_delete=models.CASCADE)
    post =models.ImageField(upload_to="story",null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    expiration_date = models.DateTimeField()
