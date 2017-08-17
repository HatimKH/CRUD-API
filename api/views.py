from rest_framework import generics

from animals.models import Dog, Cat
from .serializers import DogSerializer, CatSerializer


class DogList(generics.ListCreateAPIView):
    model = Dog
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = Dog.objects.filter(owner=self.request.user)
        return queryset

class CatList(generics.ListCreateAPIView):
    model = Cat
    serializer_class = CatSerializer

    def get_queryset(self):
        queryset = Cat.objects.filter(owner=self.request.user)
        return queryset
