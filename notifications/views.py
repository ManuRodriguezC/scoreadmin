from django.shortcuts import render
from rest_framework import viewsets
from datetime import datetime
from django.utils import timezone
from .models import *
from .serializer import EventsSerializer, NewsSerializer

class EventsApiView(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    current_date = timezone.make_aware(datetime.now())
    queryset = Event.objects.filter(date__gte=current_date)
    http_method_names = ['get']

class NewsApiView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    http_method_names = ['get']