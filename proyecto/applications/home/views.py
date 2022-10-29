from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from proyecto.applications.home.forms import PruebaForm

from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0','10','20','30']

class ListarPrueba (ListView):
    template_name = 'home/listar_prueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    fields =  ['titulo','subtitulo','cantidad']
    form_class = PruebaForm
    success_url: '/'

class ResumeFundationView(TemplateView):
    template_name = 'home/resume_foundation.html'