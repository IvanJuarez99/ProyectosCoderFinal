from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('buscar_autor/', views.buscar_autor, name='buscar_autor'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('articulos/', views.articulo_list, name='articulo_list'),
    path('buscar_categoria/', views.buscar_categoria, name='buscar_categoria'),
    path('buscar_articulos/', views.buscar_articulos, name='buscar_articulos'),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('perfil/<str:code>/', views.perfil_autor, name='perfil_autor'),
    path('articulo/editar/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('articulo/eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('eliminar_cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('about_me/', views.about_me, name='about_me'),
    path('articulo/<int:id>/', views.detalle_articulo, name='detalle_articulo'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)