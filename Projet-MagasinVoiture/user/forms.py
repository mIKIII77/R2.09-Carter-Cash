from django.forms import ModelForm
from . import models
from django import forms
from .models import Article, Piece, Ville


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        labels = {"name":"Nom de l'article", "date_ajout":"Date d'ajout de l'article", "ville":"Ville de l'article","piece":"Type de la pièce", "article_image":"L'image de l'article" }
        fields = ('name', 'date_ajout', 'ville','piece', 'article_image')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
            'date_ajout': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.Select(attrs={'class': 'form-control form-select'}),           
            'piece': forms.Select(attrs={'class': 'form-control form-select'}),
            'article_image': forms.FileInput(attrs={'class': "form-control"}),

        }

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
        labels = {"name":"Nom de la ville","describtion": "Description de la ville" }
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
            'describtion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PieceForm(ModelForm):
    class Meta: 
        model = Piece
        labels = {"name":"Nom", "describtion": "Description du type de la pièce"}
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
            'ville': forms.Select(attrs={'class': 'form-control form-select'}),
            'describtion': forms.Textarea(attrs={'class': 'form-control'}),
        }



