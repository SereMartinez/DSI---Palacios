from django.contrib import admin
from django.urls import path, include
from . import views
from applications import departamento
urlpatterns = [
    path('new-departamento/',views.NewDepartamentoForm.as_view(), name='nuevo_departamento'),
]