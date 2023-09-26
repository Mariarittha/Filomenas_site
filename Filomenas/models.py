from django.db import models

class Filomenas(models.Model):
    nome = models.CharField(max_length=150)
    