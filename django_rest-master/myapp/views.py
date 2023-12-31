from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import render
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = PostSerializer

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PublicPostListAPIView(APIView):
    def get(self, request):
        qs=Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

public_post_list=PublicPostListAPIView.as_view()

#@api_view(['GET'])
#def public_post_list(request):
#    qs=Post.objects.filter(is_public=True)
#    serializer=PostSerializer(qs, many=True)
#    return Response(serializer.data)

