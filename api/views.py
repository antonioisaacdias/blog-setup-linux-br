from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostsView(APIView):
    def get(self, request):
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)