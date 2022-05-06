from contextlib import ContextDecorator
from http.client import HTTPResponse
from multiprocessing import context
from unicodedata import name
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from pkg_resources import require
from .models import Article, Ville, Piece
from .forms import ArticleForm, VilleForm, PieceForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def home_view(request):
    tmplate = "home.html"
    return render(request, 'user/home.html')

class ArticleListView(ListView):
    model = Article
    form_class = ArticleForm
    context_object_name = 'Articles'

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm  
    success_url = reverse_lazy('Article_changelist')

def load_piece(request):
    ville_id = request.GET.get('ville')
    piece = Piece.objects.filter(ville_id=ville_id).order_by('name')
    return render(request, 'user/ville_dropdown_list_options.html', {'piece': piece})

def ArticleCreateView(request):
    ville_id = request.GET.get('ville')
    piece = Piece.objects.filter(ville_id=ville_id).order_by('name')
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Article_changelist')
        else:
            return render(request,"user/article_form.html",{"form": form, 'piece': piece})
    else :
        form = ArticleForm()
        return render(request,"user/article_form.html",{"form" : form, 'piece': piece})

def add_ville(request):
    submitted = False
    if request.method == 'POST':
        form = VilleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ville_list')
    else:
        form = VilleForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'user/add_ville.html', {'form':form, 'submitted':submitted})

def add_piece(request):
    submitted = False
    if request.method == 'POST':
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Piece_list')
    else:
        form = PieceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'user/add_piece.html', {'form':form, 'submitted':submitted})

def all_villes(request):
    ville_list = Ville.objects.all()
    return render(request, 'user/ville_list.html', {'ville_list': ville_list})

def all_pieces(request):
    piece_list = Piece.objects.all()
    return render(request, 'user/piece_list.html', {'piece_list': piece_list})

def update_ville(request, ville_id):
    ville = Ville.objects.get(pk=ville_id)
    form = VilleForm(request.POST or None, instance=ville)
    if form.is_valid():
        form.save()
        return redirect("Ville_list")
    return render(request, 'user/ville_update.html', {'ville':ville, 'form':form} )

def update_piece(request, piece_id):
    piece = Piece.objects.get(pk=piece_id)
    form = PieceForm(request.POST or None, instance=piece)
    if form.is_valid():
        form.save()
        return redirect("Piece_list")
    return render(request, 'user/piece_update.html', {'piece':piece, 'form':form} )

def delete_ville(request, ville_id):
    ville = Ville.objects.get(pk=ville_id)
    ville.delete()
    return redirect('Ville_list')

def delete_piece(request, piece_id):
    piece = Piece.objects.get(pk=piece_id)
    piece.delete()
    return redirect('Piece_list')

def delete_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('Article_changelist')

def search_article(request):
    if request.method == "POST":
        searched = request.POST['searched']
        Articles = Article.objects.filter(name__contains=searched)

        return render(request,
        'user/search_article.html',
        {'searched':searched,
        'Articles':Articles})
    else:
        return render(request,
        'user/search_article.html',
        {})