# Generated by Django 4.1.3 on 2022-11-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcer2', '0007_remove_residencia_id_alter_residencia_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencia',
            name='numero',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]