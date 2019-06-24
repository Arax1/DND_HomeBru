from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('trait_detail', args=[str(self.id)])


class RaceTrait(Trait):
    pass

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


class Classtrait(Trait):
    pass

    # foreign key to race
    # make a form for character


class Race(models.Model):

    SIZE_CHOICES = (
        ('T', "Tiny"),
        ('S', "Small"),
        ('M', "Medium"),
        ('L', "Large"),
        ('H', "Huge"),
        ('G', "Gargantuan")
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    alignment = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    speed = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # strength_mod = models.IntegerField()
    # dex_mod = models.IntegerField()
    # con_mod = models.IntegerField()
    # int_mod = models.IntegerField()
    # wis_mod = models.IntegerField()
    # cha_mod = models.IntegerField()

    # make a form for race, make this as simple as possible
    # traits = foreigh_key(RaceTrait), on_delete==CASCADE
    # abilities, features, languages, subraces,etc

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('race_detail', args=[str(self.id)])


class Character(models.Model):
    name = models.CharField(max_length=100,  default="")
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    constitution = models.IntegerField()
    dextirity = models.IntegerField()
    race_key = models.ForeignKey(Race, default=1, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])


class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hit_dice = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class_detail', args=[str(self.id)])
    # proficiencies, features, subclasses


class Background(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('background_detail', args=[str(self.id)])
    # proficiencies, languages, equipment
