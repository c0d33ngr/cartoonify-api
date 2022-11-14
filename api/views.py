from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import File
from .serializers import FileSerializer

from .transform import transform

# Create your views here.

class TransformView(APIView):


    def get(self, request, format=None):
        image_list = File.objects.all()
        serializer = FileSerializer(image_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            image_path = serializer.data.get("image")
            cartoonized_image = image_transform = transform(image_path)

            data ={"Image cartoonified":cartoonized_image}  #get image response url path

            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
