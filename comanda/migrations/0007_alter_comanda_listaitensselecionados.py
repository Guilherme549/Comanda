# Generated by Django 4.2.3 on 2023-08-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comanda', '0006_alter_comanda_listaitensselecionados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='listaItensSelecionados',
            field=models.JSONField(null=True),
        ),
    ]