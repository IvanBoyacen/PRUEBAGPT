# Generated by Django 4.1.1 on 2022-11-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codIngrediente', models.CharField(max_length=50, verbose_name='Código Ingrediente')),
                ('nomIngrediente', models.CharField(max_length=50, verbose_name='Nombre Ingrediente')),
                ('unidadMedida', models.CharField(max_length=50, verbose_name='Unidad Medida')),
                ('cantidadMateriaPrima', models.CharField(max_length=50, verbose_name='Cantidad Materia Prima')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
    ]