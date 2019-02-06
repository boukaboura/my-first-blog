from django.db import models
from django.utils import timezone


# Create your models here.
            
'''
mot clef class permet d'indiquer que nous somme en train de definir un objet
post est le nomde notre mode, le nom commence toujour par un Majuscule et
pas de caractere speciaux ou accentue ni insérer des espaces.

models.Model : signifie que Post est un modele django comme ça Django sait qu'il doit
l'enregister dans la base de données.

    models.CharField    cela nous permet de définir un champs texte avec un nombre limité
                        de caractères
    models.TextField    cela nous permet de définir un champs texte sans  limité   de caractères
                        parfait pour le contenue d'un blog post!
                        
    models.DateTimeField Définit que le champ en question est une date ou une heure
    models.ForeignKey   c'est un lien vers un autre modèls
'''
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    title  = models.CharField(max_length=200)# titre
    text = models.TextField() # text
    created_date = models.DateTimeField(blank=True, null= True) # date de creation
    published_date = models.DateTimeField(blank =True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
