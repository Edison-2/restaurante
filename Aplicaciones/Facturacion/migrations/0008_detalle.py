# Generated by Django 4.2.7 on 2024-01-16 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0007_platillo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_ed', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_ed', models.TextField()),
                ('cantidad_ed', models.IntegerField()),
                ('fecha_ed', models.DateField()),
                ('pedido_ed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Facturacion.pedido')),
                ('platillo_ed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Facturacion.platillo')),
            ],
        ),
    ]
