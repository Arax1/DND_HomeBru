# Generated by Django 2.2 on 2019-07-19 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0031_auto_20190719_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='background',
            old_name='date_created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='date_created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='date_created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='race',
            old_name='date_created',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='trait',
            old_name='date_created',
            new_name='date_posted',
        ),
    ]
