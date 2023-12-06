from django.db import models

# Create your models here.
class Apropos(models.Model):
    texte = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(max_length=255)

    def __str__(self):
        return self.text


class Galerie(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    texte = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(max_length=255)

    def __str__(self):
        return self.titre


class Avis(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(max_length=255)

    def __str__(self):
        return self.nom
    

class Partenaires(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(max_length=255)

    def __str__(self):
        return self.nom