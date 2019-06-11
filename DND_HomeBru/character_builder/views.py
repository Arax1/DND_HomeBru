from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import *


# Create your views here.


def homepage(request):
    return render(request, "home.html", {})


class RaceListView(ListView):
    model = Race
    template_name = "race_list.html"

class ClassListView(ListView):
    model  = Class
    template_name = "class_list.html"

class BackgroundListView(ListView):
    model  = Background
    template_name = "background_list.html"
