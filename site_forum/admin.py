from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Forum)
class ForumAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Topico)
class TopicoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Resposta)
class RespostaAdmin(admin.ModelAdmin):
    pass

