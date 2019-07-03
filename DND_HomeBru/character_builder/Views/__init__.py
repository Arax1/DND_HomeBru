from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from character_builder.models import Race, Class, Background, Character, Trait, RaceTrait
TEMPLATE_FOLDER = 'character_builder/'
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .Background import *
from .Character import *
from .Class import *
from .Race import *

def homepage(request):
    return render(request, "home.html", {'title': 'HomeBru - Home'})
