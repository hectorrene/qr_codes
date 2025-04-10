# Generated by Django 5.2 on 2025-04-10 14:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_orden_trabajo_remove_inventario_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
