from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('casinos.urls')),
    path('', include('subpages.urls')),  # Include subpage URLs
]

# ZEIGT KEINE MEDIA FILES AN WENN DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)