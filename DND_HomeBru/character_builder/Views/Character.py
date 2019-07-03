from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from character_builder.models import Character

TEMPLATE_FOLDER = 'character_builder/'


class CharacterListView(ListView):
    model = Character
    template_name = TEMPLATE_FOLDER + 'character_list.html'
    context_object_name = 'characters'


class CharacterDetailView(DetailView):
    model = Character
    template_name = TEMPLATE_FOLDER + 'character_detail.html'
    context_object_name = "character_details"


class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    template_name = TEMPLATE_FOLDER + 'character_create_form.html'
    fields = ['name', 'strength', 'intelligence', 'wisdom',
              'constitution', 'dextirity', 'charisma', 'race_key', 'class_key']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character
    template_name = TEMPLATE_FOLDER + 'character_update_form.html'
    fields = ['name', 'strength', 'intelligence', 'wisdom',
              'constitution', 'dextirity', 'charisma', 'race_key', 'class_key']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Character
    template_name = TEMPLATE_FOLDER + 'character_delete_form.html'
    success_url = reverse_lazy('character_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False
