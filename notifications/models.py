from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='files/')
    created_by = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=800)
    url = models.CharField(max_length=200)

class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='files/', null=True, blank=True)
    created_by = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=800)
    date = models.DateTimeField()
    
    
