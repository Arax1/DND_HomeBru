from django.test import TestCase
from django.urls import reverse
from .models import Race, Character, Class, Background
# Create your tests here.


class CharacterBuilder(TestCase):

    def setUp(self):

        self.race = Race.objects.create(
            name='test_race',
            description='testing if race model works',
            age=102,
            alignment='buggy',
            size="M",
            speed=4
        )

        self.character = Character.objects.create(
            name='test_character',
            strength=1,
            intelligence=300,
            wisdom=90,
            charisma=20,
            constitution=34,
            dextirity=11,
            race_key=self.race
        )
        # DO NOT rename class_obj to 'class'. Python will not allow this.
        self.class_obj = Class.objects.create(
            name='test_class',
            description='test_description',
            hit_dice=20
        )
        self.background = Background.objects.create(
            name='test_background',
            description='test_description'
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
        self.assertEqual(self.character.get_absolute_url(),
                         "/character_detail/1")

    def test_class_get_absolute_url(self):
        self.assertEqual(self.class_obj.get_absolute_url(), "/class_detail/1")

    def test_background_get_absolute_url(self):
        self.assertEqual(self.background.get_absolute_url(),
                         "/background_detail/1")

    def test_race_content(self):
        self.assertEqual(f'{self.race.name}', 'test_race')
        self.assertEqual(f'{self.race.description}',
                         'testing if race model works')
        self.assertEqual(self.race.age, 102)
        self.assertEqual(f'{self.race.alignment}', 'buggy')
        self.assertEqual(self.race.size, "M")
        self.assertEqual(self.race.speed, 4)

    def test_character_content(self):
        self.assertEqual(f'{self.character.name}', 'test_character')
        self.assertEqual(self.character.strength, 1)
        self.assertEqual(self.character.intelligence, 300)
        self.assertEqual(self.character.wisdom, 90),
        self.assertEqual(self.character.charisma, 20),
        self.assertEqual(self.character.constitution, 34),
        self.assertEqual(self.character.dextirity, 11),
        self.assertEqual(self.character.race_key, self.race)

    def test_class_content(self):
        self.assertEqual(f'{self.class_obj.name}', 'test_class')
        self.assertEqual(f'{self.class_obj.description}', 'test_description')
        self.assertEqual(self.class_obj.hit_dice, 20)

    def test_background_content(self):
        self.assertEqual(f'{self.background.name}', 'test_background')
        self.assertEqual(f'{self.background.description}', 'test_description')

    def test_race_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/races')
        no_response = self.client.get('/races_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'testing if race model works')
        self.assertTemplateUsed(response, "race_list.html")
        print("test_race_list_view passed")

    def test_character_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/characters')
        no_response = self.client.get('/characters_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test_character')
        self.assertTemplateUsed(response, "character_list.html")

    def test_class_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/classes')
        no_response = self.client.get('/classes_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test_class')
        self.assertTemplateUsed(response, "class_list.html")

    def test_background_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/backgrounds')
        no_response = self.client.get('/background_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test_background')
        self.assertTemplateUsed(response, "background_list.html")

    def test_race_create_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.post(reverse('race_new'), {
            'name': 'New race',
            'description': 'New race created from test module',
            'age': 22,
            'alignment': 'new_alignment',
            'size': "T",
            'speed': 13
        })
        self.assertEqual(response.status_code, 302)
        
