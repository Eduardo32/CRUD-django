# Generated by Django 2.1.7 on 2019-03-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleClientes', '0003_auto_20190310_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
