from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostsView(APIView):
    def get(self, request):
        try:
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)