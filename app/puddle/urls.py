from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from prometheus_client import make_wsgi_app
from django_prometheus import exports

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('metrics', make_wsgi_app(exports)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
