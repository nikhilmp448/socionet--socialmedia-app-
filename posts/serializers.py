from . models import Post,Story
from rest_framework import serializers
from  comments.serializers import CommentSerializer
from votes.serializers import VoteSerializer



class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    votes=VoteSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','content','post_media','category','post_date','comments','votes']

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id','post','timestamp']

