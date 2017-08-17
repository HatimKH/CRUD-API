from rest_framework import generics

from animals.models import Dog, Cat
from .serializers import DogSerializer, CatSerializer


class DogList(generics.ListCreateAPIView):
    queryset =  Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = Dog.objects.filter(owner=self.request.user)
        return queryset

class CatList(generics.ListCreateAPIView):
    queryset =  Cat.objects.all()
    serializer_class = CatSerializer

    def get_queryset(self):
        queryset = Cat.objects.filter(owner=self.request.user)
        return queryset

class RetrieveUpdateDestroyDog(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = Dog.objects.filter(owner=self.request.user)
        return queryset

class RetrieveUpdateDestroyCat(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Cat.objects.all()
    serializer_class = CatSerializer

    def get_queryset(self):
        queryset = Cat.objects.filter(owner=self.request.user)
        return queryset
