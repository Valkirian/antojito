# Generated by Django 3.1.1 on 2020-09-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200914_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='arepadehuevo',
            name='name',
            field=models.CharField(default='Arepa de Huevo', max_length=10),
        ),
        migrations.AddField(
            model_name='bollo',
            name='name',
            field=models.CharField(default='Bollo', max_length=10),
        ),
        migrations.AddField(
            model_name='carimanola',
            name='name',
            field=models.CharField(default='Carimanola', max_length=10),
        ),
        migrations.AddField(
            model_name='empanada',
            name='name',
            field=models.CharField(default='Empanada', max_length=10),
        ),
        migrations.AddField(
            model_name='salchipapa',
            name='name',
            field=models.CharField(default='Salchipapa', max_length=10),
        ),
    ]
