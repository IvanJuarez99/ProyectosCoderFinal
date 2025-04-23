from django.db import models
from django.contrib.auth.models import User
import uuid

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)
    biografia = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    code = models.CharField(max_length=36, unique=True, default=uuid.uuid4, db_index=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=20)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, related_name="comentarios", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.articulo.titulo}"