from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model=Prueba
        fields = (
            "titulo",
            "subtitulo",
            "cantidad",
        )
        wAidgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aquí'
                }
            )
        }
    def clean_cantidad (self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('El número ingresado de ser mayor a 10')
            return cantidad