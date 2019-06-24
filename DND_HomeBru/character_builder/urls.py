from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('races', RaceListView.as_view(), name="race_view"),
    path('classes', ClassListView.as_view(), name="class_view"),
    path('backgrounds', BackgroundListView.as_view(), name="background_view"),
    path('characters', CharacterListView.as_view(), name="character_view"),
    path('race_new', RaceCreateView.as_view(), name="race_new"),
    path('character_new', CharacterCreateView.as_view(), name="character_new"),
    path('class_new', ClassCreateView.as_view(), name="class_new"),
    path('character_detail/<int:pk>',
         CharacterDetailView.as_view(), name="character_detail"),
    path("background_detail/<int:pk>",
         BackgroundDetailView.as_view(), name="background_detail"),
    path('race_detail/<int:pk>', RaceDetailView.as_view(), name="race_detail"),
    path('class_detail/<int:pk>', ClassDetailView.as_view(), name="class_detail"),
    path('background_new', BackgroundCreateView.as_view(), name="background_new"),
    path('race_edit/<int:pk>', RaceUpdateView.as_view(), name="race_edit"),
    path('class_edit/<int:pk>', ClassUpdateView.as_view(), name="class_edit"),
    path('background_edit/<int:pk>', BackgroundUpdateView.as_view(), name="background_edit"),
    path('character_edit/<int:pk>', CharacterUpdateView.as_view(), name="character_edit"),
    path('race_delete/<int:pk>', RaceDeleteView.as_view(), name="race_delete"),
    path('class_delete/<int:pk>', ClassDeleteView.as_view(), name="class_delete"),
    path('background_delete/<int:pk>', BackgroundDeleteView.as_view(), name="background_delete"),
    path('character_delete/<int:pk>', CharacterDeleteView.as_view(), name="character_delete"),

]
