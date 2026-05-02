from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
import os

FRONTEND_DIR = os.path.join(settings.BASE_DIR, 'frontend')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    
    # Servir les fichiers frontend
    path('auth/login.html', serve, {'path': 'login.html', 'document_root': FRONTEND_DIR}),
    path('auth/register.html', serve, {'path': 'register.html', 'document_root': FRONTEND_DIR}),
    path('auth/dashboard.html', serve, {'path': 'dashboard.html', 'document_root': FRONTEND_DIR}),
    path('auth/style.css', serve, {'path': 'style.css', 'document_root': FRONTEND_DIR}),
    path('auth/app.js', serve, {'path': 'app.js', 'document_root': FRONTEND_DIR}),
]