# Generated by Django 4.0.5 on 2022-07-17 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recursos_alter_servico_icone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recursos',
            new_name='Recurso',
        ),
        migrations.AlterModelOptions(
            name='recurso',
            options={'verbose_name': 'Recurso', 'verbose_name_plural': 'Recursos'},
        ),
    ]
