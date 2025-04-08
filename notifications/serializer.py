from rest_framework import serializers
from .models import *

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'