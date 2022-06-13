from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['idCliente', 'nombreCliente', 'correoCliente', 'telefCliente', 'direcCliente']
        labels ={
            'idCliente': 'ID', 
            'nombreCliente': 'Nombre', 
            'correoCliente': 'Correo', 
            'telefCliente': 'Telefono',
            'direcCliente': 'Direccion',
        }
        widgets={
            'idCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id Cliente', 
                    'id': 'idCliente'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombreCliente'
                }
            ), 
            'correoCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo', 
                    'id': 'correoCliente'
                }
            ), 
            'telefCliente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Telefono',
                    'id': 'telefCliente',
                }
            ),
            'direcCliente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Direccion',
                    'id': 'direcCliente',
                }
            )

        }




 
    
class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nomProducto', 'precioProducto', 'Descripcion']
        labels ={
            'idProducto': 'ID', 
            'nomProducto': 'Nombre', 
            'precioProducto': 'Precio', 
            'Descripcion': 'Descripcion',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id Producto', 
                    'id': 'idProducto'
                }
            ), 
            'nomProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nomProducto'
                }
            ), 
            'precioProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Precio', 
                    'id': 'precioProducto'
                }
            ), 
            'Descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Descripcion',
                    'id': 'Descripcion',
                }
            )

        }   

