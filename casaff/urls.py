from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('casinos.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # Add CKEditor 5 URLs here
]

# Serve media files during development when DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)