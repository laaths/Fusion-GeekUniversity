# Generated by Django 4.0.5 on 2022-07-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipe',
            new_name='Funcionario',
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='modificados',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='modificados',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='modificados',
            new_name='modificado',
        ),
    ]
