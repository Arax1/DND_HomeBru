from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *


# Create your views here.


def homepage(request):
    return render(request, "home.html", {'title': 'HomeBru - Home'})


class RaceListView(ListView):
    model = Race
    template_name = "race_list.html"
    context_object_name = "races"


class RaceCreateView(CreateView):
    model = Race
    template_name = "race_create_form.html"
    # success_url = reverse_lazy("home")
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed', ]

class RaceDetailView(DetailView):
    model = Race
    context_object_name = "race_details"
    template_name = 'race_detail.html'

class ClassListView(ListView):
    model = Class
    template_name = "class_list.html"
    context_object_name = "classes"

class ClassCreateView(CreateView):
    model = Class
    template_name = "class_create_form.html"
    fields = ['name','description','hit_dice']
    success_url = reverse_lazy("home")

class ClassDetailView(DetailView):
    model = Class
    context_object_name = "class_details"
    template_name = 'class_detail.html'

class BackgroundListView(ListView):
    model = Background
    template_name = "background_list.html"
    context_object_name = "backgrounds"

class BackgroundCreateView(CreateView):
    model = Background
    template_name = "background_create_form.html"
    fields = ['name', 'description']
    success_url = reverse_lazy("home")

class BackgroundDetailView(DetailView):
    model = Background
    context_object_name = "background_details"
    template_name = 'background_detail.html'



class CharacterCreateView(CreateView):
    model = Character
    template_name = "character_create_form.html"
    fields = ['name','strength', 'intelligence', 'wisdom',
              'constitution', 'dextirity', 'charisma', 'race_key']
    success_url = reverse_lazy("home")


class CharacterListView(ListView):
    model = Character
    template_name = "character_list.html"
    context_object_name = 'characters'


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'character_detail.html'
    context_object_name = "character_details"
