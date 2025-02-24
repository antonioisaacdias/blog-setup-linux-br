from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import RecentPostsSerializer, HighlightedPostsSerializer, PostSerializer
from .services.post_service import get_recent_posts, get_highlighted_posts, get_post_by_slug

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

class PostView(APIView):
    def get(self, request, slug):
        post = get_post_by_slug(slug=slug)
        if not post:
            raise NotFound("Post not found with the given slug.")
        
        serialized = PostSerializer(post).data
        return Response(serialized)