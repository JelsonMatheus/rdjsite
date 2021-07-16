from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class TimeStampBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        abstract = True

class Forum(TimeStampBase):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('forum:page', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        self.slug =slugify(self.nome)
        super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Topico(TimeStampBase):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(blank=True)
    fechado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('forum:topico', kwargs={'slug':self.forum.slug, 'topico_id':self.pk})
    
    def __str__(self):
        return self.titulo

class Resposta(TimeStampBase):
    texto = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('Resposta', on_delete=models.CASCADE, null=True, blank=True)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user}-{self.pk}'
