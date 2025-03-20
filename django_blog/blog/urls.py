from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, edit_profile_view
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("edit-profile/", edit_profile_view, name="edit_profile"),
    path("", PostListView.as_view(), name="post-list"),  # View all posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # View single post
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # Create a new post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # Update post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # Delete post
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]




