# Generated by Django 5.2 on 2025-04-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_inventario_height_inventario_width'),
    ]

    operations = [
        migrations.CreateModel(
            name='etiquetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('width', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='height',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='width',
        ),
        migrations.AddField(
            model_name='inventario',
            name='orden_trabajo',
            field=models.CharField(default='', max_length=18),
        ),
    ]
