# Generated by Django 4.0.4 on 2022-06-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0004_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Descripcion',
            field=models.CharField(max_length=50, verbose_name='Descripcion'),
        ),
    ]