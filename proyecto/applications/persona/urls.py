
from django.contrib import admin
from django.urls import path, include

from . import views
from .models import Persona
from .views import ListAllPersonas, PersonaCreateView, PersonaDetailView, PersonaUpdateView, SuccessView, ListByAreaPersona, ListPersonaByKword

from django.apps import AppConfig
class PersonaConfig (AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "applications.persona"

app_name= 'persona_app'

urlpatterns = [

    path(
        '',
        views.InicioView.as_view(),
        name='Inicio'
    ),
    
    path('listar-todo-empleados/', views.ListAllPersonas.as_view()),
    path('listar-by-area/<shortname>',views.ListByAreaPersona.as_view()),
    path('buscar-empleado/', views.ListPersonasByKword.as_view()),
    path('success/', views.SuccessView.as_view()),
    path('lista-habilidades-persona/', views.ListHabilidadesPersona.as_view()),
    path('ver-persona/<pk>/',views.PersonaDetailView.as_view()),
    path('add-persona', views.PersonaCreateView.as_view()),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),
    path(
        'update-persona/<pk>/',
        views.PersonaUpdateView.as_view(),
        name='modificar_persona'
    ),
     path(
        'delete-persona/<pk>/',
        views.PersonaDeleteView.as_view(),
        name='eliminar_persona'
    ),
     path(
        'ver-persona/<pk>/',
        views.PersonaDetailView.as_view(),
        name='persona_detail'
    ),

]