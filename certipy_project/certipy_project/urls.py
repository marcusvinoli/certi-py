
from django.contrib import admin
from django.urls import path
from certipy_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('courses/', views.courses, name="Cursos"),
    path('certificates/', views.certificates, name="Certificados"),
    path('templates/', views.templates, name="Templates"),
    path('settings/', views.settings, name="Configurações"),
]
