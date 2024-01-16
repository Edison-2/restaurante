# Generated by Django 4.2.7 on 2024-01-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0008_detalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id_ed', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ed', models.CharField(max_length=100)),
                ('descripcion_ed', models.CharField(max_length=100)),
                ('unidad_medida_ed', models.CharField(max_length=20)),
                ('fecha_caducidad_ed', models.DateField()),
                ('fotografia', models.FileField(blank=True, null=True, upload_to='ingrediente')),
            ],
        ),
    ]