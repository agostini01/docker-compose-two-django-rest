from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
                'name': 'john',
                'age': 23
                }

        return Response(data)
