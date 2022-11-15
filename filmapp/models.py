from django.db import models
from django.contrib.auth.models import User


class Aktyor(models.Model):
    ism = models.CharField(max_length=50)
    jins = models.CharField(max_length=10)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=50)
    def __str__(self):return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=50)
    yil = models.PositiveSmallIntegerField()
    reyting = models.FloatField()
    janr = models.CharField(max_length=50)
    aktyorlar = models.ManyToManyField(Aktyor)
    def __str__(self):return self.nom

class Comment(models.Model):
    matn = models.CharField(max_length=100)
    sana = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE, null=True)
    def __str__(self):return self.matn