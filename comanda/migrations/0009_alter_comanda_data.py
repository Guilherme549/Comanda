# Generated by Django 4.2.3 on 2023-08-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comanda', '0008_comanda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]