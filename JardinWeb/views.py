from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import viewsets
from .serializers import ProductoSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .carrito import Carrito



# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def home(request):
    #productos =  Producto.objects.all()
    productos =  Producto.objects.filter(destacado=True)
    data = {
        'productos': productos
 }



    return render(request, 'JardinWeb/principal.html', data)

def quienessomos(request):

    return render(request,'JardinWeb/QuienesSomos.html')

def herramientas(request):
    #productos =  Producto.objects.filter(categoria_id=1)
    productos =  Producto.objects.filter(categoria_id=1)
    data = {
        'productos': productos
 }
    
    return render(request,'JardinWeb/herramientas.html',data)

def plantas(request):
    productos =  Producto.objects.filter(categoria_id=2)
    data = {
        'productos': productos
 }
    return render(request,'Jardinweb/plantas.html',data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST' :
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

 

    return render(request,'registration/registro.html',data)

def listadodonadores(request):
    return render(request,'Jardinweb/listadonadores.html')

@permission_required('Jardineriaweb.add_producto')
def panel(request):
    return render(request,'Jardinweb/panel.html')

@permission_required('Jardineriaweb.add_producto')
def agregar(request):
    data = {
    'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado correctamente")
            data["mensaje"] = "Guardado Correctamente"
        else:
            data ["form"] = formulario

    return render(request,'Jardinweb/agregar.html',data)

@permission_required('Jardineriaweb.add_producto')
def listar(request):
    productos =  Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos,10)
        productos= paginator.page(page)
    except:
        raise Http404
    data = {
        'productos': productos,
        'paginator': paginator
 }
   
    return render(request,'Jardinweb/listar.html',data)
   
@permission_required('Jardineriaweb.add_producto')
def modificar(request, id):
    producto=get_object_or_404(Producto,idProducto=id) 
    data={
        'form':ProductoForm(instance=producto)
    }
        
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto modificado correctamente")
            data["mensaje"] = "Producto modificado correctamente"
        else:
            data ["form"] = formulario
            
            return redirect(to="listar")

        data ["form"] = formulario
    return render(request,'Jardinweb/modificar.html',data)
    
@permission_required('Jardineriaweb.add_producto')
def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,idProducto=id) 
    producto.delete() 
    return redirect(to="listar")

#funciones carro
def agregar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar_producto(producto)
    return redirect(to="/home")


def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Home")

def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Home")


def carrito(request):

    return render(request,'JardinWeb/carrito.html')
