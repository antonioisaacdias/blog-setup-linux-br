from rest_framework import serializers
from .models import Post

class RecentPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'subject', 'author', 'resume', 'created_at', 'image']

class HighlightedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'subject', 'image']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'subject', 'author', 'resume', 'content', 'created_at', 'updated_at', 'image']