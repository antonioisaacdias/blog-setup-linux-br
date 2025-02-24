from rest_framework import serializers
from .models import Post

class RecentPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'subject', 'author', 'resume', 'created_at', 'image']

class HighlightedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'subject', 'image']