# Generated by Django 4.2.20 on 2025-04-14 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mantencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dueño', models.CharField(max_length=100)),
                ('patente', models.CharField(max_length=10)),
                ('kilometraje', models.PositiveIntegerField()),
                ('tipo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(blank=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('proceso', 'En proceso'), ('finalizada', 'Finalizada')], default='pendiente', max_length=20)),
            ],
        ),
    ]
