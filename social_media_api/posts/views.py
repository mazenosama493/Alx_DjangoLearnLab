from rest_framework import viewsets, generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404  # ✅ Correct import
from django.contrib.auth import get_user_model

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification

CustomUser = get_user_model()


class PostPagination(PageNumberPagination):
    """Pagination settings for posts."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    """CRUD operations for posts."""
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        """Ensure post is associated with the logged-in user."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """CRUD operations for comments."""
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Ensure comment is associated with the logged-in user."""
        serializer.save(author=self.request.user)


class LikePostView(generics.CreateAPIView):
    """Allows users to like a post."""
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Handle liking a post."""
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ Correct usage
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        if request.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked!"}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.DestroyAPIView):
    """Allows users to unlike a post."""
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        """Handle unliking a post properly."""
        post = generics.get_object_or_404(Post, pk=kwargs.get("pk"))  # ✅ Correct usage
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({"detail": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Like removed."}, status=status.HTTP_204_NO_CONTENT)


class UserFeedView(generics.ListAPIView):
    """Retrieve posts from users the authenticated user follows."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get posts from followed users."""
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        """Return serialized posts."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
