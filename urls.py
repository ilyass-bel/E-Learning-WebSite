from django.urls import path
from . import views

urlpatterns = [
    path('etudiant/',views.etudiant, name='Etudiant'),
    path('enseignant/', views.enseignant, name='Enseignant'),
    path('ajouter_cours/', views.ajouter_cours, name='ajouter_cours'),
    path('ajouter_contenu/', views.ajouter_contenu, name='ajouter_contenu'),
    path('update_cours/<str:pk>/', views.updateCours, name='update_cours'),
    path('supprimer_cours/<str:pk>/', views.supprimerCours, name='supprimer_cours'),
    path('ajouter_traveaux/', views.ajouterTraveux, name='ajouter_traveaux'),
    path('update_traveaux/<str:pk>/', views.updateTraveaux, name='update_traveaux'),
    path('supprimer_traveaux/<str:pk>/', views.supprimerTraveux, name='supprimer_traveaux'),
    path('rendus_etudiants/', views.rendus_etudiants, name='rendus_etudiants'),
    path('ajouter_rendu/', views.ajouter_rendu, name='ajouter_rendu'),
    path('supprimer_rendu/<str:pk>/', views.supprimer_rendu, name='supprimer_rendu'),
    path('ajouter_Question/', views.ajouter_Question, name='ajouter_Question'),
    path('boite_reception/', views.boite_reception, name='boite_reception'),
    path('ajouter_Reponse/', views.ajouter_Reponse, name='ajouter_Reponse'),
    path('boite_reponse/', views.boite_reponse, name='boite_reponse'),
    path('traveaux_prof/', views.traveaux_prof, name='traveaux_prof'),
    path('rendu_etu/', views.rendu_etu, name='rendu_etu'),
]