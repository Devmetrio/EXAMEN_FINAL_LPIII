"""
URL configuration for AMES_ExamenFinal_Parte1Site project.

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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from miapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.personas, name = "personas"),
    path('agregar_persona/', views.agregar_persona, name = "agregar_persona"),
    path('personas/', views.personas, name = "personas"),
    path('registro_persona/', views.registrar_persona, name='registro_persona'),
    path('agregar_persona/<int:persona_id>/', views.registrar_persona, name='editar_persona'),
    path('eliminar_persona/<int:persona_id>/', views.eliminar_persona, name='eliminar_persona'),
]
