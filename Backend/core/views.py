from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post
from .serial import RegisterSerializer, PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    def post(self, request):
        return Response({'message': 'Login logic placeholder'})

class HomeView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    print(queryset)

class AboutView(APIView):
    def get(self, request):
        return Response({"message": "This is the About Page"})

class LikePostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, pk): # 🔥 IMPORTANT!
        post = get_object_or_404(Post, pk=pk)
        post.likes += 1
        post.save()
        return Response({'likes': post.likes}, status=status.HTTP_200_OK)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
