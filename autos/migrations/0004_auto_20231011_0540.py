# Generated by Django 3.1.3 on 2023-10-11 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_auto_20231010_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=100, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('direccion', models.TextField(blank=True, verbose_name='Direccion')),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autos.propietario'),
        ),
    ]