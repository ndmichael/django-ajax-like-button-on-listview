from django.urls import path
from .views import PostListView, PostDetailView, post_like
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view()),
    path('details/<int:pk>/', PostDetailView.as_view()),
    path('like/', post_like, name='post_like'),
]

