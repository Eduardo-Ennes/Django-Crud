# Generated by Django 5.0.4 on 2024-06-05 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_profissao_contato_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='mostar_perfil',
            new_name='mostrar_perfil',
        ),
    ]
