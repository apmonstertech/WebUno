from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
