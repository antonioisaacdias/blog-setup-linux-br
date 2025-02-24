from django.urls import path
from .views import IndexView, PostView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('post/<str:post_title>/', PostView.as_view(), name='post')
]