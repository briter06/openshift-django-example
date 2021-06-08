from django.db import models

class Persona(models.Model):
    nombre = models.TextField()
    edad = models.IntegerField()
