# Generated by Django 3.0.9 on 2020-08-04 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_coleccion_prenda'),
        ('products', '0004_auto_20200804_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.Seccion_Cliente'),
        ),
    ]