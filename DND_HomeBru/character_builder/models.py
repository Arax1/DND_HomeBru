from django.db import models

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    Alighment = models.CharField(max_length=100)
    Size = models.IntegerField()
    Speed = models.IntegerField()
    # abilities, features, languages, subraces,etc


class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hit_dice = models.IntegerField()
    # proficiencies, features, subclasses


class Background(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # proficiencies, languages, equipment
