# Generated by Django 2.2 on 2019-06-06 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='background',
            old_name='background_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='class_name',
            new_name='name',
        ),
    ]
