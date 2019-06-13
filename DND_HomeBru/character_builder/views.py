from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *


# Create your views here.


def homepage(request):
    return render(request, "home.html", {})


class RaceListView(ListView):
    model = Race
    template_name = "race_list.html"
    context_object_name = "races"


class RaceCreateView(CreateView):
    model = Race
    template_name = "race_create_form.html"
    success_url = reverse_lazy("home")
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed', ]


class ClassListView(ListView):
    model = Class
    template_name = "class_list.html"
    context_object_name = "classes"


class BackgroundListView(ListView):
    model = Background
    template_name = "background_list.html"
    context_object_name = "backgrounds"


class CharacterCreateView(CreateView):
    model = Character
    template_name = "character_create_form.html"
    fields = ['strength', 'intelligence', 'wisdom',
              'constitution', 'dextirity', 'charisma', 'race_key']
    success_url = reverse_lazy("home")
