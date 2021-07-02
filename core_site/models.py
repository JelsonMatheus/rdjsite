from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.
class Forum:
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)

class Categoria:
    nome = models.CharField(max_length=30)

class Topico:
    titulo = models.CharField(max_length=50)
    texto = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True, blank=True)

class Resposta:
    texto = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)