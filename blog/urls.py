from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view()),
    path('details/<int:pk>/', PostDetailView.as_view()),
]