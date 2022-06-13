from django.urls import path 
from .views import index, somos, galeria, contacto, api, form_1, mostrarcli, form_crear_cliente, form_mod_cliente, form_del_cliente, form_crear_producto, mostrarprod, form_mod_producto, form_del_producto

urlpatterns=[ 
    path ('', index, name="index"),
    path ('somos/', somos, name="somos"),
    path ('galeria/', galeria, name="galeria"),
    path ('contacto/', contacto, name="contacto"),
    path ('form_1/', form_1, name="form_1"),
    path ('api_feriado/', api, name="api_feriado"),
    path ('mostrarcli/', mostrarcli, name="mostrarcli"),
    path ('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path ('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path ('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path ('form_crear_producto/', form_crear_producto, name="form_crear_producto"),
    path ('mostrarprod/', mostrarprod, name="mostrarprod"),
    path ('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
]