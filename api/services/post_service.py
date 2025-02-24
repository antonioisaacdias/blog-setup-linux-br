from api.models import Post

def get_recent_posts(limit):
    return Post.objects.order_by('-created_at')[:limit]

def get_highlighted_posts():
    return Post.objects.filter(is_highlighted=True)