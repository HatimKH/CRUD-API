from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from animals.models import Dog, Cat
from .serializers import DogSerializer, CatSerializer


class DogList(APIView):
    def get(self, request, format=None):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

class CatList(APIView):
    def get(self, request, format=None):
        cats = Cat.objects.all()
        serializer = DogSerializer(cats, many=True)
        return Response(serializer.data)
