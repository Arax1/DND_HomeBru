# Generated by Django 2.2 on 2019-06-13 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0005_character_race_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classtrait',
            fields=[
                ('trait_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character_builder.Trait')),
            ],
            bases=('character_builder.trait',),
        ),
        migrations.CreateModel(
            name='RaceTrait',
            fields=[
                ('trait_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character_builder.Trait')),
            ],
            bases=('character_builder.trait',),
        ),
    ]
