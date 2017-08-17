from django.conf.urls import url, include
from django.contrib import admin
from .views import DogList, CatList, RetrieveUpdateDestroyDog, RetrieveUpdateDestroyCat

urlpatterns = [
    url(r'^dogs/$', DogList.as_view(),name='dogs-list'),
    url(r'^dogs/(?P<pk>\d+)/$', RetrieveUpdateDestroyDog.as_view(), name='dog-detail'),
    url(r'^cats/$', CatList.as_view(),name='cats-list'),
    url(r'^cats/(?P<pk>\d+)/$', RetrieveUpdateDestroyCat.as_view(), name='cat-detail'),
]
