from importlib.util import module_from_spec
from django.db import models
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField


class Empleado(models.Model):

    JOB_CHOICES = (
                  ('0','Contador'),
                  ('1','Administrador'),
                  ('2','Economista'),
                  ('3','Otro'),
                  )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField(max_length=60)
    full_name=models.CharField(
      'Nombre Completo',
      max_length=120,
      blank=True)
    
    job= models.CharField('Trabajo',max_length=50, choices = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
     
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida= RichTextField() 
    class Meta:
      verbose_name = 'Mi Empleado'
      verbose_name_plural = 'Empleados de la Empresa'
      ordering = ['-first_name', 'last_name']
      unique_together = ('first_name', 'last_name') 

    def __str__ (self):
        return str(self.id)+', '+self.first_name+', '+self.last_name

