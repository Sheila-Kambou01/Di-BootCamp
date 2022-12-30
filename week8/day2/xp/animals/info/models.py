from django.db import models

# Create your models here.
class Animal(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    pattes = models.IntegerField()
    poid = models.IntegerField()
    taille = models.IntegerField()
    vitess = models.IntegerField()
    famille = models.IntegerField()


class Famille(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    nom = models.CharField(max_length=200, null=True)
