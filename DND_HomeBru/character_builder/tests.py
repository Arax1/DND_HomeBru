from django.test import TestCase
from .models import Race, Character, Class, Background
# Create your tests here.
class Chracter_Builder(TestCase):
    def setup(self):
        self.race  = Race.objects.create(
        name = 'test_race',
        description= 'testing if race model works',
        age = 102,
        alignment=  'buggy',
        size = 14,
        speed = 4
        )
        self.character = Character.objects.create(
        name = 'test_character',
        strength = 1,
        intelligence = 300,
        wisdom = 90,
        charisma = 20,
        constitution = 34,
        dextirity = 11,
        race_key = self.race
        )
        self.class = Class.objects.create(
        name = 'test_class',
        description = 'test_description',
        hit_dice = 20
        )
        self.background = Background.objects.create(
        name = 'test_background',
        description = 'test_description'
        )
        
