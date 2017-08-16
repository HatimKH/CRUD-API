from django.conf.urls import url, include
from django.contrib import admin
from .views import DogList, CatList

urlpatterns = [
    url(r'^dogs/', DogList.as_view(),name='dogs-list'),
    url(r'^cats/', CatList.as_view(),name='cats-list'),
]
