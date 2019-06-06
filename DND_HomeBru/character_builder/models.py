from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class RaceTrait(Trait):



class FEAT(Trait):


class Feature(Trait):


class ASI(Feature):




class Character(Models.model):
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    Wisdom = models.IntegerField()
    Charisma = models.IntegerField()
    Constitution = models.IntegerField()
    Dextirity = models.IntegerField()
    # foreign key to race
    # make a form for character 

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    Alighment = models.CharField(max_length=100)
    Size = models.IntegerField()
    Speed = models.IntegerField()
    # make a form for race, make this as simple as possible
    # traits = foreigh_key(RaceTrait), on_delete==CASCADE
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
