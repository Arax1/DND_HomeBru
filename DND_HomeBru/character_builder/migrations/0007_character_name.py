# Generated by Django 2.2 on 2019-06-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0006_classtrait_racetrait_trait'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
