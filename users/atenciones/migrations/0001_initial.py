# Generated by Django 4.1.7 on 2023-02-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('fecha_atencion', models.DateField()),
                ('documento', models.CharField(max_length=255)),
                ('orden', models.CharField(max_length=255)),
                ('historia', models.CharField(max_length=50)),
                ('observaciones', models.TextField()),
                ('tipo_novedad', models.CharField(max_length=50)),
                ('novedad', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
