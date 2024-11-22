from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from .views import*

router = routers.DefaultRouter()
router.register(f'eventos-score', EventsApiView, 'eventos')
router.register(f'noticias-score', NewsApiView, 'noticias')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path("docs/", include_docs_urls(title="Turns API")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)