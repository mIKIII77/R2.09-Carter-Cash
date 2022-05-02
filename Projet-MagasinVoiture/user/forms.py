from django.forms import ModelForm
from . import models
from django import forms
from .models import Article, Piece, Ville


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        labels = {"name":"Nom de l'article", "date_ajout":"Date d'ajout de l'article", "ville":"Ville de l'article","piece":"Type de la pièce" }
        fields = ('name', 'date_ajout', 'ville','piece')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['piece'].queryset = Piece.objects.none()

        if 'ville' in self.data:
            try:
                ville_id = int(self.data.get('ville'))
                self.fields['piece'].queryset = Piece.objects.filter(ville_id=ville_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['piece'].queryset = self.instance.ville.piece_set.order_by('name')

class VilleForm(ModelForm):
    class Meta: 
        model = Ville
        labels = {"name":"Nom"}
        fields = "__all__"

class PieceForm(ModelForm):
    class Meta: 
        model = Piece
        labels = {"name":"Nom"}
        fields = "__all__"



