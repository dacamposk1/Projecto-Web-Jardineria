from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

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

def plantas2(request):
    return render(request,'Jardinweb/plantas2.html')


def registro(request):
    return render(request,'Jardinweb/registro.html')

def listadodonadores(request):
    return render(request,'Jardinweb/listadonadores.html')

def panel(request):
    return render(request,'Jardinweb/panel.html')

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

def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,idProducto=id) 
    producto.delete() 
    return redirect(to="listar")