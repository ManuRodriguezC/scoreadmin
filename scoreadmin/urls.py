from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('notificaciones/', include('notifications.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', RedirectView.as_view(url='admin'))
]

# Servir archivos estáticos en desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Servir archivos de medios en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)