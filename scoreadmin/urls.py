from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('notificaciones/', include('notifications.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', RedirectView.as_view(url='admin'))
]
