# Generated by Django 5.0.2 on 2024-03-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_clcliente_options_alter_clcliente_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clcliente',
            name='rut',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
