from django.test import TestCase
from django.urls import reverse
from .models import Race, Character, Class, Background
# Create your tests here.
class Character_Builder(TestCase):
    def setUp(self):
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
        # DO NOT rename class_obj to 'class'. Python will not allow this.
        self.class_obj = Class.objects.create(
        name = 'test_class',
        description = 'test_description',
        hit_dice = 20
        )
        self.background = Background.objects.create(
        name = 'test_background',
        description = 'test_description'
        )
    def test_race_string_representation(self):
        self.assertEqual(str(self.race), self.race.name)

    def test_character_string_representation(self):
        self.assertEqual(str(self.character), self.character.name)

    def test_class_string_representation(self):
        self.assertEqual(str(self.class_obj), self.class_obj.name)

    def test_background_string_representation(self):
        self.assertEqual(str(self.background), self.background.name)

    def test_race_get_absolute_url(self):
        self.assertEqual(self.race.get_absolute_url(), "/race_detail/1")

    def test_character_get_absolute_url(self):
        self.assertEqual(self.character.get_absolute_url(), "/character_detail/1")

    def test_class_get_absolute_url(self):
        self.assertEqual(self.class_obj.get_absolute_url(), "/class_detail/1")

    def test_background_get_absolute_url(self):
        self.assertEqual(self.background.get_absolute_url(), "/background_detail/1")
