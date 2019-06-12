from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class RaceTrait(Trait):
    pass


class Classtrait(Trait):
    pass


class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    alignment = models.CharField(max_length=100)
    size = models.IntegerField()
    speed = models.IntegerField()

    # strength_mod = models.IntegerField()
    # dex_mod = models.IntegerField()
    # con_mod = models.IntegerField()
    # int_mod = models.IntegerField()
    # wis_mod = models.IntegerField()
    # cha_mod = models.IntegerField()

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
