from rest_framework import generics 
from ..models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class PostListView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticated,)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticated,)
				