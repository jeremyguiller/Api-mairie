from django.shortcuts import render
from rest_framework import viewsets
from .models import Location,Image,Administrateur,Texte
from .serializers import Locationserializer,ImageSerializers,AdministrateurSerializers,TexteSerializers


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('name')
    serializer_class = Locationserializer

class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all().order_by('name')
    serializer_class = AdministrateurSerializers

class TexteViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('name')
    serializer_class = TexteSerializers

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('name')
    serializer_class = ImageSerializers