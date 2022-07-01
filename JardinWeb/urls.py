from django.urls import path, include
from .views import home,quienessomos,herramientas,plantas,registro,listadodonadores,agregar,listar,modificar,\
panel,eliminar_producto,ProductoViewset ,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito,carrito
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('',home,name="home"),
    path('Jardineria/Quienes_Somos/',quienessomos,name="quienessomos"),
    path('Jardineria/herramientas/',herramientas,name="herramientas"),
    path('Jardineria/plantas/',plantas,name="plantas"),
    path('registration/registro/',registro,name="registro"),
    path('Jardineria/listadodonadores/',listadodonadores,name="listadodonadores"),
    path('Jardineria/agregar/',agregar,name="agregar"),
    path('Jardineria/listar/',listar,name="listar"),
    path('Jardineria/modificar/<id>/',modificar,name="modificar"),
    path('eliminar_producto/<id>',eliminar_producto,name="eliminar_producto"),
    path('Jardineria/panel/',panel,name="panel"),
    path('api/', include(router.urls)),
    path('agregar/<producto_id>/', agregar_producto, name="Add"),   
    path('eliminar_producto/<producto_id>/', eliminar_producto, name="Delete"),
    path('restar/<producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="Cls"),
    path('Jardineria/carrito/',carrito,name="carrito"),

]
