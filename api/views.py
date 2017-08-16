from rest_framework import generics

from animals.models import Dog, Cat
from .serializers import DogSerializer, CatSerializer


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
