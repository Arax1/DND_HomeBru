from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Race


# Create your views here.


def homepage(request):
    return render(request, "home.html", {})


class RaceListView(ListView):
    model = Race
    template_name = "race_list.html"
