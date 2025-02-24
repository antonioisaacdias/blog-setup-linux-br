from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecentPostsSerializer, HighlightedPostsSerializer
from .services.post_service import get_recent_posts, get_highlighted_posts

class IndexView(APIView):
    def get(self, request):
        try:
            recent_posts = get_recent_posts(5)
            serializer_recents = RecentPostsSerializer(recent_posts, many=True).data

            highlighted_posts = get_highlighted_posts(3)
            serializer_highlighted = HighlightedPostsSerializer(highlighted_posts, many=True).data

            others_posts = get_recent_posts(3)
            serializer_others = RecentPostsSerializer(others_posts, many=True).data

            response_data = {
                'recent_posts': serializer_recents,
                'highlighted_posts': serializer_highlighted,
                'others_posts': serializer_others
            }

            return Response(response_data)

        except Exception as e:
            return Response({'error': str(e)}, status=400)