"""
URL configuration for aurora_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from auth_perms.views import LoginView, RegisterView, ProfileView, salir


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('auth_perms.urls')),
    path('areas-app/', include('areas.urls')),
    path('clients-app/', include('clients.urls')),
    path('materials-app/', include('materials.urls')),
    path('entrances-app/', include('entrances.urls')),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('logout/', salir, name='logout'),
    
]
