# Generated by Django 4.0.4 on 2022-06-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del Cliente')),
                ('nombreCliente', models.CharField(max_length=20, verbose_name='Nombre del Cliente')),
                ('correoCliente', models.EmailField(max_length=254, verbose_name='Correo del Cliente')),
                ('telefCliente', models.IntegerField(max_length=9, verbose_name='Numero del Cliente')),
                ('direcCliente', models.CharField(max_length=30, verbose_name='Direccion del Cliente')),
            ],
        ),
    ]