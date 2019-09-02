# Generated by Django 2.2 on 2019-07-23 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0003_auto_20190723_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving_Throw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_posted', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=300)),
                ('Class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='saves', to='character_builder.Class')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
