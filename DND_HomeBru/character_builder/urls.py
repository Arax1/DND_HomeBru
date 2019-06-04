from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('races', views.RaceListView.as_view(), name="race_view")
]
