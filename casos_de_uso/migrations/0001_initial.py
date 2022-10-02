# Generated by Django 3.2.15 on 2022-10-02 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(help_text='Un rol son los distintos usuarios que interactuan con el sistema. Ejemplo: Gerente de ventas, el cliente, proveedor, empleado, recepcionista, etc.', max_length=50, verbose_name='Rol del actor')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actores', to='proyectos.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Descripción de la tarea o actividad que realiza el actor')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='casos_de_uso.actor')),
            ],
        ),
    ]
