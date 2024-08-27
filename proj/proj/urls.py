from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('words/', include('word.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)