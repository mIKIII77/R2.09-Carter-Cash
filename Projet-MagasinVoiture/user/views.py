from http.client import HTTPResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Article, Ville, Piece
from .forms import ArticleForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

class ArticleListView(ListView):
    model = Article
    form_class = ArticleForm
    context_object_nom_piece = 'Article'

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('Article_changelist')

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm  
    success_url = reverse_lazy('Article_changelist')

def load_ville(request):
    ville_id = request.GET.get('ville')
    piece = Piece.objects.filter(ville_id=ville_id).order_by('name')
    return render(request, 'user/ville_dropdown_list_options.html', {'Ville': Ville})
