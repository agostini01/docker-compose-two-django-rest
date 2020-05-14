from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post


class TestView(APIView):

    permission_classes = [IsAuthenticated,]

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
