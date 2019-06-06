from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('races', views.RaceListView.as_view(), name="race_view"),
    path('classes', views.ClassListView.as_view(), name="class_view"),
    path('backgrounds', views.BackgroundListView.as_view(), name="background_view")
]
