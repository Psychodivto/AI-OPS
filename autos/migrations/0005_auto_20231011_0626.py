# Generated by Django 3.1.3 on 2023-10-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0004_auto_20231011_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='ano',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='auto',
            name='kilometraje',
            field=models.IntegerField(max_length=100),
        ),
    ]
