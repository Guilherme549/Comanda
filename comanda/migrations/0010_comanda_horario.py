# Generated by Django 4.2.3 on 2023-08-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comanda', '0009_alter_comanda_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='horario',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
