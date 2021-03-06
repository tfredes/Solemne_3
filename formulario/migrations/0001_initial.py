# Generated by Django 3.1.2 on 2020-12-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('apellido', models.TextField(max_length=50)),
                ('rut', models.CharField(max_length=20)),
                ('nserie', models.CharField(max_length=20)),
                ('region', models.IntegerField(choices=[(1, 'Region de Arica y Parinacota'), (2, 'Region de Tarapaca'), (3, 'Región de Antofagasta'), (4, 'Región de Atacama'), (5, 'Región de Coquimbo'), (6, 'Región de Valparaíso'), (7, 'Región Metropolitana de Santiago'), (8, 'Región del Libertador General Bernardo OHiggins'), (9, 'Región del Maule'), (10, 'Región de Ñuble'), (11, 'Región del Biobío'), (12, 'Región de La Araucanía'), (13, 'Región de Los Ríos'), (14, 'Región de Los Lagos'), (15, 'Región de Aysén'), (16, 'Región de Magallanes y de la Antártica Chilena')])),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
