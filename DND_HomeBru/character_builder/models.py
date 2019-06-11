from django.db import models


# class Trait(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

# class RaceTrait(Trait):
#
#
#
# class FEAT(Trait):
#
#
# class Feature(Trait):
#
#
# class ASI(Feature):
#




    # foreign key to race
    # make a form for character

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    alignment = models.CharField(max_length=100)
    size = models.IntegerField()
    speed = models.IntegerField()
    # make a form for race, make this as simple as possible
    # traits = foreigh_key(RaceTrait), on_delete==CASCADE
    # abilities, features, languages, subraces,etc

    def __str__(self):
        return self.name

class Character(models.Model):
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    constitution = models.IntegerField()
    dextirity = models.IntegerField()
    race_key = models.ForeignKey(Race, default=1,on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hit_dice = models.IntegerField()

    # proficiencies, features, subclasses


class Background(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # proficiencies, languages, equipment
