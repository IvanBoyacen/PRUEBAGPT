# Generated by Django 4.1.5 on 2023-02-21 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0003_remove_receta_fkcodcomponente_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecetaDetalle',
        ),
    ]
