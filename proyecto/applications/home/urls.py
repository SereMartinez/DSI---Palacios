from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'resume-foundation/',
        views.ResumeFoundationView.as_view(),
        name='resume_foundation'
        ),
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('listar-prueba/',views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(),name='prueba_add'),
]