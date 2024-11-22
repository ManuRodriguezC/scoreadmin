from django.contrib import admin
from .models import *

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by', 'paragraph', 'date']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by', 'paragraph', 'url']