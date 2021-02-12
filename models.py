from django.db import models
from datetime import datetime


class Contenu(models.Model):
    content = models.FileField(upload_to='ressources/cours/')
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE)

    def __str__(self):
        return self.cours.titre


class Cours(models.Model):
    titre = models.CharField(max_length=100)
    filiere = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now(), verbose_name="Date de parution")
    semestre = models.CharField(max_length=10)

    def __str__(self):
        return self.titre


class Traveaux(models.Model):
    nomT = models.CharField(max_length=100)
    dateT = models.DateTimeField(default=datetime.now)
    semestre = models.CharField(max_length=10)
    filiere = models.CharField(max_length=255)
    travail = models.FileField(upload_to='ressources/traveaux/')

    def __str__(self):
        return self.nomT


class Rendus(models.Model):
    nomT = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    semestre = models.CharField(max_length=10)
    filiere = models.CharField(max_length=255)
    rendu = models.FileField(upload_to='ressources/rendus')

    def __str__(self):
        return self.nomT


class Question(models.Model):
    nom_complet = models.CharField(max_length=200)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_complet


class Reponse(models.Model):
    nom_completP = models.CharField(max_length=200)
    reponse = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_completP