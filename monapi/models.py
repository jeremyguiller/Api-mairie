from django.db import models

# Create your models here.

class Location(models.Model) :
    date = models.CharField(max_length=50)
    name = models.CharField(max_length=60)
    confirmer = models.BooleanField()
    

    def __str__(self):
        return self.name
    
class Administrateur(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=50)
    mdp = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Texte(models.Model) :
    intitule = models.CharField(max_length=50)
    texte = models.TextField(max_length=50000)
    
    def __str__(self):
        return self.name

class Image(models.Model) :
    description = models.CharField(max_length=50)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
