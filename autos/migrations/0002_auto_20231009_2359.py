# Generated by Django 3.1.3 on 2023-10-09 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='modelo',
            field=models.CharField(max_length=100),
        ),
    ]
