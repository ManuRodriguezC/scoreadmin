from django.contrib import admin
from .models import *

@admin.register(Evento)
class EventAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'imagen', 'creadoPor', 'parrafo', 'fecha', 'lugar']

@admin.register(Noticia)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'imagen', 'creadoPor', 'parrafo', 'url']