from django.urls import include, path
from . import views

urlpatterns = [
    path('articles', views.ArticleListView.as_view(), name='Article_changelist'),
    path('add/', views.ArticleCreateView, name='Article_add'),
    path('<int:pk>/', views.ArticleUpdateView.as_view(), name='Article_change'),
    path('ajax/load-piece/', views.load_piece, name='ajax_load_piece'),
    path('add_ville', views.add_ville, name="Ville_add"),
    path('add_piece', views.add_piece, name="Piece_add"),
    path('all_villes', views.all_villes, name="Ville_list"),
    path('all_pieces', views.all_pieces, name="Piece_list"),
    path('update_ville/<ville_id>', views.update_ville, name="Ville_update"),
    path('update_piece/<piece_id>', views.update_piece, name="Piece_update"),
    path('delete_ville/<ville_id>,', views.delete_ville, name="Ville_delete"),
    path('delete_piece/<piece_id>,', views.delete_piece, name="Piece_delete"),
    path('delete_article/<article_id>,', views.delete_article, name="Article_delete"),
    path('', views.home_view, name="Home"),
    path('search_article', views.search_article, name="Article_recherche"),
    path('show_ville/<ville_id>', views.show_ville, name="Show_ville"),
    path('show_piece/<piece_id>', views.show_piece, name="Show_piece"),
    path('show_article/<article_id>', views.show_article, name="Show_article"),


   ]