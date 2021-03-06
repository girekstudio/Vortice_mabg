# Generated by Django 3.0.9 on 2020-11-06 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(default=0)),
                ('offer', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('stock', models.BooleanField(default=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('imagen_2', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('imagen_3', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('imagen_4', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('talla', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=999)),
                ('precio_oferta', models.DecimalField(blank=True, decimal_places=2, max_digits=999, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('articulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.Articulo')),
                ('prenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.Prenda')),
            ],
            options={
                'verbose_name_plural': '1. Producto ',
            },
        ),
    ]
