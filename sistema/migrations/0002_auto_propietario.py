# Generated by Django 5.0.1 on 2024-01-20 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('matricula', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('adquisicion', models.DateField()),
                ('imagen_matricula', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.auto')),
            ],
        ),
    ]