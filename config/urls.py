from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from biddings.views import room
from core.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('biddings/', include('biddings.urls')),
    path('', index_view, name='index'),
    path('<str:room_name>/', room, name='room'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
