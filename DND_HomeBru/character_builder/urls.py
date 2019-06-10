from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name="home"),
    path('races', RaceListView.as_view(), name="race_view"),
    path('classes', ClassListView.as_view(), name="class_view"),
    path('backgrounds', BackgroundListView.as_view(), name="background_view"),
    path('race_new', RaceCreateView.as_view(), name="race_new"),
    path('character_new', CharacterCreateView.as_view(), name="character_new" )
]
