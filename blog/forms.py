from django import forms
from .models import Autor, Categoria, Articulo, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
    'username': 'No se permiten espacios, tildes (á, é, í, ó, ú) ni símbolos especiales como #, !, &, *.',
}

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    contenido = forms.CharField(
        max_length=200,
        label='Link de GitHub',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'https://github.com/tu_usuario/repositorio'
        })
    )

    nueva_categoria = forms.CharField(max_length=50, required=False, label="Nueva Categoría")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label="Categoría",empty_label="Seleccione una categoría" )
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria']

class BusquedaArticuloForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Buscar Artículo')


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['avatar']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido'] 

    contenido = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Escribe tu comentario...',
        'rows': 4,
        'class': 'comentario-textarea',
    }))