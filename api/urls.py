from django.urls import path
from .views import RecentPostsView

urlpatterns = [
    path('recent-posts/', RecentPostsView.as_view(), name='recent-posts')
]