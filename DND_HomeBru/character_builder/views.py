# comment
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Race, Class, Background, Character
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# homepage view


def homepage(request):
    return render(request, "home.html", {'title': 'HomeBru - Home'})

# view listing all races


class RaceListView(ListView):
    model = Race
    template_name = "race_list.html"
    context_object_name = "races"

# view creating the races


class RaceCreateView(LoginRequiredMixin, CreateView):
    model = Race
    template_name = "race_create_form.html"
    # success_url = reverse_lazy("home")
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Race
    template_name = 'race_update_form.html'
    # success_url = reverse_lazy('home')
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        race = self.get_object()

        if self.request.user == race.author:
            return True

        return False


class RaceDetailView(DetailView):
    model = Race
    context_object_name = "race_details"
    template_name = 'race_detail.html'


class RaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Race
    template_name = 'race_delete_form.html'
    success_url = reverse_lazy('race_view')

    def test_func(self):
        race = self.get_object()

        if self.request.user == race.author:
            return True

        return False


class ClassListView(ListView):
    model = Class
    template_name = "class_list.html"
    context_object_name = "classes"


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    template_name = "class_create_form.html"
    fields = ['name', 'description', 'hit_dice']
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassUpdateView(UpdateView):
    model = Class
    template_name = 'class_update_form.html'
    fields = ['name', 'description', 'hit_dice']


class ClassDetailView(DetailView):
    model = Class
    context_object_name = "class_details"
    template_name = 'class_detail.html'


class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'class_delete_form.html'
    success_url = reverse_lazy('home')


class BackgroundListView(ListView):
    model = Background
    template_name = "background_list.html"
    context_object_name = "backgrounds"


class BackgroundCreateView(CreateView):
    model = Background
    template_name = "background_create_form.html"
    fields = ['name', 'description']
    success_url = reverse_lazy("home")


class BackgroundUpdateView(UpdateView):
    model = Background
    template_name = 'background_update_form.html'
    fields = ['name', 'description']


class BackgroundDetailView(DetailView):
    model = Background
    context_object_name = "background_details"
    template_name = 'background_detail.html'


class BackgroundDeleteView(DeleteView):
    model = Background
    template_name = 'background_delete_form.html'
    success_url = reverse_lazy('home')


class CharacterCreateView(CreateView):
    model = Character
    template_name = "character_create_form.html"
    fields = ['name', 'strength', 'intelligence', 'wisdom',
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


class CharacterUpdateView(UpdateView):
    model = Character
    template_name = 'character_update_form.html'
    fields = ['name', 'strength', 'intelligence', 'wisdom',
              'constitution', 'dextirity', 'charisma', 'race_key']


class CharacterDeleteView(DeleteView):
    model = Character
    template_name = 'character_delete_form.html'
    success_url = reverse_lazy('home')
