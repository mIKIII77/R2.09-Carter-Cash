from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='Article_changelist'),
    path('add/', views.ArticleCreateView.as_view(), name='Article_add'),
    path('<int:pk>/', views.ArticleUpdateView.as_view(), name='Article_change'),
    path('ajax/load-ville/', views.load_ville, name='ajax_load_piece'),
   ]