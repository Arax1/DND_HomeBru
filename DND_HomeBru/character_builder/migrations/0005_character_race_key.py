# Generated by Django 2.2 on 2019-06-10 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0004_auto_20190610_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='race_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='character_builder.Race'),
        ),
    ]
