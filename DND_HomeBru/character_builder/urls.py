from django.urls import path

from .Views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('races', RaceListView.as_view(), name="race_view"),
    path('classes', ClassListView.as_view(), name="class_view"),
    path('backgrounds', BackgroundListView.as_view(), name="background_view"),
    path('characters', CharacterListView.as_view(), name="character_view"),
    path('race/new', RaceCreateView.as_view(), name="race_new"),
    path('character/new', CharacterCreateView.as_view(), name="character_new"),
    path('class/new', ClassCreateView.as_view(), name="class_new"),
    path('character/detail/<int:pk>',
         CharacterDetailView.as_view(), name="character_detail"),
    path("background/detail/<int:pk>",
         BackgroundDetailView.as_view(), name="background_detail"),
    path('race/detail/<int:pk>', RaceDetailView.as_view(), name="race_detail"),
    path('class/detail/<int:pk>', ClassDetailView.as_view(), name="class_detail"),
    path('background/new', BackgroundCreateView.as_view(), name="background_new"),
    path('race/edit/<int:pk>', RaceUpdateView.as_view(), name="race_edit"),
    path('class/edit/<int:pk>', ClassUpdateView.as_view(), name="class_edit"),
    path('background/edit/<int:pk>', BackgroundUpdateView.as_view(), name="background_edit"),
    path('character/edit/<int:pk>', CharacterUpdateView.as_view(), name="character_edit"),
    path('race/delete/<int:pk>', RaceDeleteView.as_view(), name="race_delete"),
    path('class/delete/<int:pk>', ClassDeleteView.as_view(), name="class_delete"),
    path('background/delete/<int:pk>', BackgroundDeleteView.as_view(), name="background_delete"),
    path('character/delete/<int:pk>', CharacterDeleteView.as_view(), name="character_delete"),
    path('race/trait/new', RaceTraitCreateView.as_view(), name='race_trait_new'),
    path('race/traits', RaceTraitListView.as_view(), name='race_trait_view'),
    path('race/trait/edit/<int:pk>', RaceTraitUpdateView.as_view(), name='race_trait_edit'),
    path('race/trait/delete/<int:pk>', RaceTraitDeleteView.as_view(), name= 'race_trait_delete'),
    path('race/trait/detail/<int:pk>', RaceTraitDetailView.as_view(), name= 'race_trait_detail'),


]
