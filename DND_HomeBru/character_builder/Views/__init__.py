from .Race import *
from .Class import *
from .Character import *
from .Background import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from character_builder.models import Race, Class, Background, Character, Trait, RaceTrait
TEMPLATE_FOLDER = 'character_builder/'


def homepage(request):
    return render(request, "home.html", {'title': 'HomeBru - Home'})


class UserContentListView(ListView):
    model = Race
    template_name = 'profile_content.html'

    def get_context_data(self, **kwargs):
        context = super(UserContentListView, self).get_context_data(**kwargs)

        user = get_object_or_404(User, username=self.kwargs.get('username'))

        race_list = Race.objects.filter(author=user)
        class_list = Class.objects.filter(author=user)
        background_list = Background.objects.filter(author=user)

        context['all_objects'] = [*race_list, *class_list, *background_list]
        context['user'] = user
        return context
