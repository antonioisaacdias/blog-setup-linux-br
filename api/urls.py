from django.urls import path
from .views import IndexView, PostView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('post/<str:slug>/', PostView.as_view(), name='full_post')
]