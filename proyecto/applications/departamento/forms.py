from django import forms

from proyecto.applications.departamento.models import Departamento
class NewDepartamentoForm (forms.Form):
    nombre=forms.CharField(max_length=50)
    apellidos=forms.CharField(max_length=50)
    departamento=forms.CharField(max_length=20)
    shortname=forms.CharField(max_length=20)

    