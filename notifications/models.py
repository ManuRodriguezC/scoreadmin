from django.db import models
from .sendMessages import send_global_notification
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='files/')
    creadoPor = models.CharField(max_length=200)
    parrafo = models.CharField(max_length=800)
    url = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            try:
                title = "Tenemos una nueva noticia, ven!"
                content = f"Conoce sobre {self.titulo}"
                image = f"https://manudev2024.pythonanywhere.com/{self.imagen.url}"
                response = send_global_notification(titulo=title, contenido=content, image=image)
                logger.info(f"Notificación enviada para News ID {self.pk}: {response}")
            except ObjectDoesNotExist:
                logger.error(f"Error: El objeto News ID {self.pk} aún no está completamente guardado.")
            except Exception as e:
                logger.error(f"Error al enviar la notificación para News ID {self.pk}: {str(e)}")

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='files/', null=True, blank=True)
    creadoPor = models.CharField(max_length=200)
    parrafo = models.CharField(max_length=800)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            try:
                title = f"Nuevo evento!, {self.titulo}"
                content = f"Este {self.fecha} tendremos un evento, no te lo pierdas!"
                image = self.imagen.url
                send_global_notification(titulo=title, contenido=content, image=image)
            except ObjectDoesNotExist:
                print("Error: El objeto aún no está completamente guardado.")
    

