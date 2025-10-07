from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Temas
    path('', views.lista_temas, name='lista_temas'),
    path('tema/nuevo/', views.crear_tema, name='crear_tema'),
    path('tema/<int:pk>/', views.detalle_tema, name='detalle_tema'),
    path('tema/<int:pk>/editar/', views.editar_tema, name='editar_tema'),
    path('tema/<int:pk>/eliminar/', views.eliminar_tema, name='eliminar_tema'),

    # Respuestas
    path('tema/<int:tema_id>/respuesta/nuevo/', views.crear_respuesta, name='crear_respuesta'),
    path('respuesta/<int:pk>/editar/', views.editar_respuesta, name='editar_respuesta'),
    path('respuesta/<int:pk>/eliminar/', views.eliminar_respuesta, name='eliminar_respuesta'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)