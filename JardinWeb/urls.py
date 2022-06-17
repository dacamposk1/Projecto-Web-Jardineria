from django.urls import path
from .views import home,quienessomos,herramientas,plantas,plantas2,registro,listadodonadores,agregar,listar,modificar, panel,eliminar_producto 


urlpatterns = [
    path('',home,name="home"),
    path('Jardineria/Quienes_Somos/',quienessomos,name="quienessomos"),
    path('Jardineria/herramientas/',herramientas,name="herramientas"),
    path('Jardineria/plantas/',plantas,name="plantas"),
    path('Jardineria/plantas2/',plantas2,name="plantas2"),
    path('Jardineria/registro/',registro,name="registro"),
    path('Jardineria/listadodonadores/',listadodonadores,name="listadodonadores"),
    path('Jardineria/agregar/',agregar,name="agregar"),
    path('Jardineria/listar/',listar,name="listar"),
    path('Jardineria/modificar/<id>/',modificar,name="modificar"),
    path('eliminar_producto/<id>',eliminar_producto,name="eliminar_producto"),
    path('Jardineria/panel/',panel,name="panel"),
    
]
