from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import File
from .serializers import FileSerializer

# Create your views here.

class TransformView(APIView):

    def get(self, request, format=None):
        image_list = File.objects.all()

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)

