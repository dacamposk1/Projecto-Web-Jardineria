from django.contrib import admin

from .models import Categoria, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display =["idProducto","nombreProducto", "marca","descripcion", "precio"]
    search_fields=["nombre"]
    list_filter=["marca"]
    list_per_page=15
admin.site.register(Categoria)
admin.site.register(Producto,ProductoAdmin)
