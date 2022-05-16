from distutils.command.upload import upload
from pydoc import describe
from django.db import models


class Ville(models.Model):
    name = models.CharField(max_length=30)
    describtion = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Piece(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    describtion = models.CharField(max_length=500)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    date_ajout = models.DateField(null=True, blank=True)
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True)
    piece = models.ForeignKey(Piece, on_delete=models.SET_NULL, null=True)
    article_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name