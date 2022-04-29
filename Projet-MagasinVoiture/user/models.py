from django.db import models


class Ville(models.Model):
    name = models.CharField(max_length=30)

    def str(self):
        return self.name

class Piece(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def str(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    date_ajout = models.DateField(null=True, blank=True)
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True)
    piece = models.ForeignKey(Piece, on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.name 

    def dico(self):
        return {"ville" : self.ville, "piece" : self.piece, "date_ajout" : self.date_ajout}