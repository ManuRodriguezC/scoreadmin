from django.shortcuts import render
from rest_framework import viewsets
from django.utils import timezone
from datetime import datetime
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializer import EventsSerializer, NewsSerializer

class EventsApiView(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    current_date = timezone.make_aware(datetime.now())
    queryset = Evento.objects.filter(fecha__gte=current_date).order_by('-id')
    http_method_names = ['get']

class NewsApiView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = Noticia.objects.all().order_by('-id')
    http_method_names = ['get']