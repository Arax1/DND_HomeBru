from django.urls import path

from .Views import *

urlpatterns = [
    path('', homepage, name="home"),

    # Paths for Race Views
    path('races', RaceListView.as_view(), name="race_view"),
    path('race/new', RaceCreateView.as_view(), name="race_new"),
    path('race/detail/<int:pk>', RaceDetailView.as_view(), name="race_detail"),
    path('race/edit/<int:pk>', RaceUpdateView.as_view(), name="race_edit"),
    path('race/delete/<int:pk>', RaceDeleteView.as_view(), name="race_delete"),

    # Paths for Race Trait Views
    path('race/detail/new/<int:pk>',
         RaceTraitCreateView.as_view(), name='race_trait_new'),
    path('race/trait/edit/<int:pk>/<int:rpk>',
         RaceTraitUpdateView.as_view(), name='race_trait_edit'),
    path('race/trait/delete/<int:pk>',
         RaceTraitDeleteView.as_view(), name='race_trait_delete'),

    # Paths for Class Views
    path('classes', ClassListView.as_view(), name="class_view"),
    path('class/new', ClassCreateView.as_view(), name="class_new"),
    path('class/detail/<int:pk>', ClassDetailView.as_view(), name="class_detail"),
    path('class/edit/<int:pk>', ClassUpdateView.as_view(), name="class_edit"),
    path('class/delete/<int:pk>', ClassDeleteView.as_view(), name="class_delete"),

    # Paths for Background Views
    path('backgrounds', BackgroundListView.as_view(), name="background_view"),
    path("background/detail/<int:pk>",
         BackgroundDetailView.as_view(), name="background_detail"),
    path('background/new', BackgroundCreateView.as_view(), name="background_new"),
    path('background/edit/<int:pk>',
         BackgroundUpdateView.as_view(), name="background_edit"),
    path('background/delete/<int:pk>',
         BackgroundDeleteView.as_view(), name="background_delete"),

    # Paths for Background Views
    path('characters', CharacterListView.as_view(), name="character_view"),
    path('character/new', CharacterCreateView.as_view(), name="character_new"),
    path('character/detail/<int:pk>',
         CharacterDetailView.as_view(), name="character_detail"),
    path('character/edit/<int:pk>',
         CharacterUpdateView.as_view(), name="character_edit"),
    path('character/delete/<int:pk>',
         CharacterDeleteView.as_view(), name="character_delete"),

    # Other Paths
    path('user/<str:username>',
         UserContentListView.as_view(), name="profile_content")


]
