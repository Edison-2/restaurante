# Generated by Django 4.2.7 on 2024-01-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0010_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='categoria_ed',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
