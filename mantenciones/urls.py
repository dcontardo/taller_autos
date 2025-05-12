from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mantenciones, name='lista_mantenciones'),
    path('crear/', views.crear_mantencion, name='crear_mantencion'),
    path('editar/<int:id>/', views.editar_mantencion, name='editar_mantencion'),
    path('eliminar/<int:id>/', views.eliminar_mantencion, name='eliminar_mantencion'),
]
