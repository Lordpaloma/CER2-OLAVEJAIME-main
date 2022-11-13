# Generated by Django 4.1.3 on 2022-11-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=30)),
                ('fecha_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]
