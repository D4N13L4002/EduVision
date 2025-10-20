
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Endpoints de visión
    path("api/vision/", include("api.urls_vision")),

    # Endpoints de flashcards
    path("api/flashcards/", include("api.urls_flashcards")),

    # Si tienes otros módulos, agrégalos aquí igual:
    # path("api/object-game/", include("api.urls_object_game")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
