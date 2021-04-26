from rest_framework import serializers , fields
from .models import Location,Texte,Image,Administrateur


class Locationserializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateTimeField()
    class Meta:
         model = Location
         fields = ('date','name','confirmer')
         

class AdministrateurSerializers(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Administrateur
        fields = ('name','email','mdp')

class TexteSerializers(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Texte
        fields = ('intitule','texte')

class ImageSerializers(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Image
        fields = ('description','image')