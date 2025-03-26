from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserSerializer

CustomUser = get_user_model()

class UserListView(generics.ListAPIView):
    """Retrieve a list of all users."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FollowUserView(APIView):
    """Allow an authenticated user to follow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            request.user.follow_user(user_to_follow)
            return Response({"message": "You are now following this user."}, status=HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=HTTP_400_BAD_REQUEST)

class UnfollowUserView(APIView):
    """Allow an authenticated user to unfollow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.unfollow_user(user_to_unfollow)
            return Response({"message": "You have unfollowed this user."}, status=HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=HTTP_400_BAD_REQUEST)

class UserFeedView(generics.GenericAPIView):
    """Retrieve posts from followed users."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = request.user.get_following_posts()
        serialized_posts = [{"id": post.id, "title": post.title, "content": post.content, "author": post.author.username} for post in posts]
        return Response(serialized_posts, status=HTTP_200_OK)


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data})

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        return Response({'token': response.data['token'], 'user': UserSerializer(user).data})
    
