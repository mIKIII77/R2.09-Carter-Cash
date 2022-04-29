from django.forms import ModelForm
from . import models
from django import forms
from .models import Article, Piece


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'date_ajout', 'ville','piece')

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['piece'].queryset = Piece.objects.none()

        if 'ville' in self.data:
            try:
                ville_id = int(self.data.get('ville'))
                self.fields['piece'].queryset = Piece.objects.filter(ville_id=ville_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['piece'].queryset = self.instance.ville.piece_set.order_by('name')