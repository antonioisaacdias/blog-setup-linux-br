from api.models import Post

def get_recent_posts(limit):
    return Post.objects.order_by('-created_at')[:limit]

def get_highlighted_posts(limit):
    return Post.objects.filter(is_highlighted=True).order_by('-created_at')[:limit]

def get_post_by_slug(slug):
    try:
        return Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return None
