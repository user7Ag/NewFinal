# Generated by Django 4.2.7 on 2023-11-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('telefono', models.CharField(max_length=64)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDelPlato', models.CharField(max_length=64)),
                ('descripcionDelPlato', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Suministros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreIngrediente', models.CharField(max_length=64)),
                ('nombreBebidas', models.CharField(max_length=64)),
            ],
        ),
    ]