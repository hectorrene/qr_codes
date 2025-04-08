# Generated by Django 5.2 on 2025-04-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieza', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
