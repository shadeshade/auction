from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Register, Login, Logout

app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
