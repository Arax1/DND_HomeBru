# Generated by Django 2.2 on 2019-07-01 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0019_trait_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='author',
        ),
    ]
