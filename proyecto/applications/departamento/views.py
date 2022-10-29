from django.shortcuts import render
from django.views.generic.edit import FormView
from proyecto.applications import departamento

from proyecto.applications.departamento.models import Departamento

from .forms import NewDepartamentoForm

class NewDepartamentoView(FormView):
    template_name= 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print ('********ESTAMOS EN FORM VALID***********')

        depa = Departamento(
            name= form.cleaned_data['departamento'],
            short_name= form.cleaned_data['shorname'],
        )

        depa.save()

        nombre= form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos'],
        Persona.objects.create(
            first_name=nombre,
            last_name=apellidos[0],
            job='1',
            departamento=depa,
        )
        return super(NewDepartamentoForm,self).form_valid(form)


