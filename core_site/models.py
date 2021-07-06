from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.

class TimeStampMixin():
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Forum(models.Model, TimeStampMixin):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

class Topico(models.Model, TimeStampMixin):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(blank=True)
    fechado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True, blank=True)

class Resposta(models.Model, TimeStampMixin):
    texto = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)