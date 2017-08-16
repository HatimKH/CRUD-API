# -*- coding: utf-8 -*-
from rest_framework import serializers
from animals.models import Dog, Cat


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = (
            'id',
            'name',
            'birthday',
            'owner',
        )

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = (
            'id',
            'name',
            'birthday',
            'owner',
        )
