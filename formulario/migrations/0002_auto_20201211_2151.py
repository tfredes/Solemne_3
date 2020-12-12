# Generated by Django 3.1.2 on 2020-12-12 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='region',
            field=models.IntegerField(choices=[(1, 'Region de Arica y Parinacota'), (2, 'Region de Tarapaca'), (3, 'Región de Antofagasta'), (4, 'Región de Atacama'), (5, 'Región de Coquimbo'), (6, 'Región de Valparaíso'), (7, 'Región Metropolitana de Santiago'), (8, 'Región del Libertador General Bernardo OHiggins'), (9, 'Región del Maule'), (10, 'Región de Ñuble'), (11, 'Región del Biobío'), (12, 'Región de La Araucanía'), (13, 'Región de Los Ríos'), (14, 'Región de Los Lagos'), (15, 'Región de Aysén'), (16, 'Región de Magallanes y de la Antártica Chilena')], default=7),
        ),
    ]