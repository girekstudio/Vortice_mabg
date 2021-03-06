# Generated by Django 3.0.9 on 2020-11-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='youtube',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(blank=True, help_text='360x360', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen_2',
            field=models.ImageField(blank=True, help_text='360x360', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen_3',
            field=models.ImageField(blank=True, help_text='360x360', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen_4',
            field=models.ImageField(blank=True, help_text='360x360', null=True, upload_to='media'),
        ),
    ]
