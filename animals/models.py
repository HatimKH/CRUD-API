# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name
