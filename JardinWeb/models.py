from django.db import models

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto=models.CharField(primary_key=True,max_length=10, verbose_name='id producto')
    nombreProducto=models.CharField(max_length=100, verbose_name='nombre producto')
    marca=models.CharField(max_length=100, verbose_name="Marca")
    descripcion= models.TextField(max_length=1000, null=True, blank=True, verbose_name='descripcion')
    precio= models.IntegerField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    oferta= models.BooleanField(null=True)
    destacado=models.BooleanField(null=True)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self): 
        return self.nombreProducto