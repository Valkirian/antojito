# Generated by Django 3.1.1 on 2020-09-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200914_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arepadehuevo',
            name='name',
            field=models.CharField(default='Arepa de Huevo', max_length=20),
        ),
    ]