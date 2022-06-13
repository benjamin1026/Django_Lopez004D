from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def somos(request):
    return render (request, 'somos.html')
def galeria(request):
    return render (request, 'galeria.html')
def form_1(request):
    return render (request, 'form_1.html')
def contacto(request):
    return render (request, 'contacto.html')
def api(request):
    return render (request, 'api_feriado.html')
def form_crear_cliente(request):
    return render (request, 'form_crear_cliente.html')

def form_crear_producto(request):
    return render (request, 'form_crear_producto.html')


#clientes

def mostrarcli(request):

    clientes = Cliente.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request, 'mostrarcli.html', datos)

def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()        #similar al insert
            return redirect('mostrarcli')
    else:
        cliente_form=ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})



def form_mod_cliente(request, id):
    cliente =Cliente.objects.get(idCliente=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrarcli')

    return render(request, 'form_mod_cliente.html', datos)

def form_del_cliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    cliente.delete()
    return redirect('mostrarcli')


#productos

def mostrarprod(request):

    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'mostrarprod.html', datos)

def form_crear_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()        #similar al insert
            return redirect('mostrarprod')
    else:
        producto_form=ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

def form_mod_producto(request, id):
    producto =Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrarprod')

    return render(request, 'form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('mostrarprod')

