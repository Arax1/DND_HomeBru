from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

DEFAULT_CLASS_ID = 1

"""

"""


class Trait(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(config_name='HOMEBRU_EDITOR')
    date_posted = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trait_detail', args=[str(self.id)])
    class Meta:
        abstract = True


class RaceTrait(Trait):
    race = models.ForeignKey('Race', on_delete=models.CASCADE, related_name='traits')
    def get_absolute_url(self):
        return reverse('race_trait_detail', args=[str(self.id)])


class BackgroundTrait(Trait):
    background = models.ForeignKey('Background', on_delete=models.CASCADE, related_name='traits')


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


"""
The classtrait model is equivelant to what is known as 'class features' in the DND
conventional cannon.
"""

class Classtrait(Trait):
    unlock_level = models.PositiveIntegerField(default=1)
    Class  = models.ForeignKey('Class', default  =DEFAULT_CLASS_ID ,on_delete=models.CASCADE, related_name='features')


class Saving_Throw(Trait):
    description = None
    Class  = models.ForeignKey('Class', default  =DEFAULT_CLASS_ID ,on_delete=models.CASCADE, related_name='saves')


class Proficiency(Trait):
    description = models.CharField(max_length=300)
    Class  = models.ForeignKey('Class', default  =DEFAULT_CLASS_ID ,on_delete=models.CASCADE, related_name='proficiencies')
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
    description = RichTextField(config_name='HOMEBRU_TEXT_EDITOR')
    age = models.IntegerField()
    alignment = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='M')
    speed = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='races')
    date_posted = models.DateField(auto_now=True)
    # Make this part of RaceTrait

    # make a form for race, make this as simple as possible
    # traits = foreigh_key(RaceTrait), on_delete==CASCADE
    # abilities, features, languages, subraces,etc

    def __str__(self):
        return self.name

    # def get_traits_choices(self):

    def get_absolute_url(self):
        return reverse('race_detail', args=[str(self.id)])


class Class(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(config_name='HOMEBRU_TEXT_EDITOR')
    hit_dice = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

#another class Class called SpellCaster that will inherit from class??

    def get_absolute_url(self):
        return reverse('class_detail', args=[str(self.id)])
    # proficiencies, features, subclasses

class Background(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(config_name='HOMEBRU_TEXT_EDITOR')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backgrounds')
    date_posted = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('background_detail', args=[str(self.id)])
    # proficiencies, languages, equipment


class Character(models.Model):
    name = models.CharField(max_length=100,  default="")
    level = models.PositiveIntegerField(default=1)
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    constitution = models.IntegerField()
    dextirity = models.IntegerField()
    race_key = models.ForeignKey(Race, default=1, on_delete=models.CASCADE,related_name='character')
    class_key = models.ForeignKey(Class, default=1, on_delete=models.CASCADE, related_name='character')
    background  = models.ForeignKey(Background, default=1, on_delete=models.CASCADE, related_name='character')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character')
    date_posted = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])
