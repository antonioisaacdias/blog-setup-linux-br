from rest_framework import serializers
from .models import Post

class HTMLField(serializers.CharField):
   def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Converta o conteúdo, caso necessário
        representation['content'] = str(instance.content)  # Garantir que o conteúdo seja string
        return representation
    

class PostSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    
    class Meta:
        model = Post
        fields = ['title', 'subject', 'author', 'content', 'created_at', 'updated_at', 'is_highlighted']
