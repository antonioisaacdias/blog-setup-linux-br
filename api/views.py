from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import RecentPostsSerializer

class RecentPostsView(APIView):
    def get(self, request):
        try:
            # Buscar os 5 posts mais recentes
            queryset = Post.objects.all().order_by('-created_at')[:5]
            
            # Serializar o queryset
            serializer = RecentPostsSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)