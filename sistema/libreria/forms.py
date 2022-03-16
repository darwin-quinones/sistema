from django import forms

from .models import Libro

# utilizacion de formularios
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'