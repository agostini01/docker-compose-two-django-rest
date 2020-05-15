from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


class PostViewManual(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Handles POST and GET methods."""
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateView(generics.CreateAPIView):
    """Handles only POST methods."""
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostView(generics.ListCreateAPIView):
    """Handles POST and GET methods methods."""
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TestView(APIView):
    """Manual way to create the api for POST and GET."""

    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()

        # Serialize all the posts
        # serializer = PostSerializer(qs, many=True)

        # Serialize single instance
        post = qs.first()
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
