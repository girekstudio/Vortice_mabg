# Generated by Django 3.0.9 on 2020-08-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200804_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='oferta',
        ),
        migrations.AddField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='talla',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]