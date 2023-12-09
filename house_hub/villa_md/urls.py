from django.urls import path
from . import views
urlpatterns = [
    path("mesi/",  views.CreaMese.as_view(), name="crea_mese"),
    path('mese/<int:pk>/crea-giornata/', views.crea_orelavoro, name="crea_giornata"),
    path('mese/<int:pk>/', views.visualizza_mese, name="mese_view"),
    path('mese/', views.HomeVilla.as_view(), name="homevilla"),
    path('orario/<int:pk>/', views.visualizza_orario, name="visualizza_orario"),
    path('orario/<int:pk>/aggiungi/', views.aggiungi_attivita, name="aggiungi_a_lavoro"),
    path('azione/<int:pk>/', views.visualizza_attivita, name="lista_attivita"),
    path("interventi/",  views.CreaIntervento.as_view(), name="crea_intervento"),
    path('intervento/', views.ListaInterventi.as_view(), name="lista_interventi"),
    ]