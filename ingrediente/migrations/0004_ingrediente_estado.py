# Generated by Django 4.1.5 on 2023-02-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0003_alter_ingrediente_codingrediente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
