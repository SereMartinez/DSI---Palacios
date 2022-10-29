from ast import Delete
import re
from django.shortcuts import render
#full full ffffull importaciones de las clases
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Empleado, Persona

class ListAllPersonas (ListView):
    template_name = "proyecto/list_all.html"
    paginate_by = 4
    ordering = 'first_name'
    model = Persona
    context_object_name='lista'

class SuccessView (TemplateView):
    template_name= 'proyecto/success.html'
# def def get_queryset(self):
#     palabra_clave = self.request.GET.get("kword",'')
#     lista = Empleado.objects.filter(
#         first_name__incontains=palabra_clave
#     )
#     return lista
class ListByAreaPersona(ListView):
    template_name= 'proyecto/list_by_area.html'

    # queryset=Persona.objects.filter(departamento_name='Area Contable')
    # context_object_name = 'lista'
    def get_queryset(self):
        lista = Persona.objects.filter(departamento_short='Área Administracion')
        return lista

class ListPersonaByKword(ListView):
    template_name = 'proyecto/by_kword.html'
    context_object_name = 'lista'
    def get_queryset(self):
        print('------rayitarayitarayitarayita------')
        palabra_clave = self.request.GET.get("kword", '')
        print ("===igualigualigual===",palabra_clave)
        lista = Persona.objects.filter(first_name=palabra_clave)
        print('LISTA RESULTADO: ', lista)
        return lista

class ListHabilidadesPersona(ListView):
    template_name= 'proyecto/habilidades.html'
    context_object_name = 'Habilidades'

    def get_queryset (self):
        persona = Persona.object.get(id=2)
        return persona.Habilidades.all ()

class PersonaDetailView(DetailView):
    model = Persona
    template_name= 'proyecto/detail_persona.html'
    context_object_name = 'lista'

class PersonaDetailView(CreateView):
    model = Persona
    template_name= 'proyecto/add.html'
    fields =  ['first_name','last_name','job']

class PersonaCreateView (CreateView):
    model= Persona
    template_name = 'proyecto/add.html'
    fields = ['first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')

def form_valid(self, form):
    persona = form.save()
    persona.full_name = persona.first_name + ' '+ persona.last_name
    persona.save()
    return super(PersonaCreateView, self).form_valid(form)

class SuccessView(TemplateView):
    template_name="proyecto/sucess.html"

class PersonaUpdateView (UpdateView):
    model = Persona
    template_name = 'persona/update.html'
    fields = ['first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print ('******* METODO POST*********')
        print ('****************************')
        return super().post(request, *args, **kwargs  )


    def form_valid(self, form):
        
        print ('******* METODO form_valid*********')
        print ('****************************')
        return super(PersonaUpdateView).form_valid(form  )
        

class PersonaDeleteView (DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:correcto')

class InicioView(TemplateView):
    template_name = "inicio.html"