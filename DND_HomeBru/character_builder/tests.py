from django.test import TestCase
from django.urls import reverse
from .models import Race, Character, Class, Background, User
# Create your tests here.
TEMPLATE_FOLDER = 'character_builder/'
SUCCESS_CODE = 404
NO_RESPONSE_CODE = 200
REDIRECT_CODE = 302
class CharacterBuilder(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(
        'Lee',
        'Lee@blues.com',
        'redpassword'
        )
        self.race = Race.objects.create(
            name='test_race',
            description='testing if race model works',
            age=102,
            alignment='buggy',
            size="M",
            speed=4,
            author=self.author
        )

        self.character = Character.objects.create(
            name='test_character',
            strength=1,
            intelligence=300,
            wisdom=90,
            charisma=20,
            constitution=34,
            dextirity=11,
            race_key=self.race,
            author=self.author
        )
        # DO NOT rename class_obj to 'class'. Python will not allow this.
        self.class_obj = Class.objects.create(
            name='test_class',
            description='test_description',
            hit_dice=20,
            author=self.author
        )
        self.background = Background.objects.create(
            name='test_background',
            description='test_description',
            author=self.author
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
        self.assertEqual(self.race.get_absolute_url(), "/race/detail/1")

    def test_character_get_absolute_url(self):
        self.assertEqual(self.character.get_absolute_url(),
                         "/character/detail/1")

    def test_class_get_absolute_url(self):
        self.assertEqual(self.class_obj.get_absolute_url(), "/class/detail/1")

    def test_background_get_absolute_url(self):
        self.assertEqual(self.background.get_absolute_url(),
                         "/background/detail/1")

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
        self.assertEqual(response.status_code, NO_RESPONSE_CODE)
        self.assertEqual(no_response.status_code, SUCCESS_CODE)
        self.assertContains(response, 'testing if race model works')
        self.assertTemplateUsed(response, TEMPLATE_FOLDER + "race_list.html")
        print("test_race_list_view passed")

    def test_character_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/characters')
        no_response = self.client.get('/characters_1')
        self.assertEqual(response.status_code, NO_RESPONSE_CODE)
        self.assertEqual(no_response.status_code, SUCCESS_CODE)
        self.assertContains(response, 'test_character')
        self.assertTemplateUsed(response,TEMPLATE_FOLDER + "character_list.html")

    def test_class_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/classes')
        no_response = self.client.get('/classes_1')
        self.assertEqual(response.status_code, NO_RESPONSE_CODE)
        self.assertEqual(no_response.status_code, SUCCESS_CODE)
        self.assertContains(response, 'test_class')
        self.assertTemplateUsed(response,TEMPLATE_FOLDER +  "class_list.html")

    def test_background_list_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.get('/backgrounds')
        no_response = self.client.get('/background_1')
        self.assertEqual(response.status_code, NO_RESPONSE_CODE)
        self.assertEqual(no_response.status_code, SUCCESS_CODE)
        self.assertContains(response, 'test_background')
        self.assertTemplateUsed(response, TEMPLATE_FOLDER + "background_list.html")

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
        self.assertEqual(response.status_code, REDIRECT_CODE)


    def test_background_create_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.post(reverse('background_new'), {
            'name': 'New background',
            'description': 'New background created from test module',
            'author':self.author
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_class_create_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.post(reverse('class_new'), {
            'name': 'New background',
            'description': 'New background created from test module',
            'hit_dice':76,
            'author':self.author
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_character_create_view(self):
        # print("primary key:" + str(self.post.url))
        response = self.client.post(reverse('class_new'), {
            'name': 'New background',
            'level':76,
            'strength':100,
            'intelligence':87,
            'wisdom':110,
            'charisma':95,
            'constitution':45,
            'dextirity':65,
            'race_key':self.race,
            'class_key':self.class_obj,
            'author':self.author
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_background_update_view(self):
        response = self.client.post(reverse('background_edit', args='1'),{
        'name': 'Updated background_name',
        'description': 'Updated description'
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_class_update_view(self):
        response = self.client.post(reverse('class_edit', args='1'),{
        'name': 'Updated class_name',
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)


    def test_character_update_view(self):
        response = self.client.post(reverse('character_edit', args='1'),{
        'name': 'Updated character_name',
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)


    def test_race_update_view(self):
        response = self.client.post(reverse('race_edit', args='1'),{
        'name': 'Updated race_name',
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_race_delete_view(self):
        response = self.client.get(
        reverse('race_delete', args='1'))
        # print('redirect for race_delete:' + response['location'])
        self.assertEqual(response.status_code, REDIRECT_CODE)


    def test_character_delete_view(self):
        response = self.client.get(
        reverse('character_delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_class_delete_view(self):
        response = self.client.get(
        reverse('class_delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_background_delete_view(self):
        response = self.client.get(
        reverse('background_delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
