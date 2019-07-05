from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from character_builder.models import Race, RaceTrait

TEMPLATE_FOLDER = 'character_builder/'


class RaceListView(ListView):
    model = Race
    template_name = TEMPLATE_FOLDER + 'race_list.html'
    context_object_name = "races"

    # def get_context_data(self, **kwargs):
    #     context = super(RaceListView, self).get_context_data(**kwargs)
    #     context['race_traits'] = RaceTrait.objects.filter(race=self.get_object())
    #     return context


class RaceDetailView(DetailView):
    model = Race
    context_object_name = "race_details"
    template_name = TEMPLATE_FOLDER + 'race_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RaceDetailView, self).get_context_data(**kwargs)
        context['race_traits'] = RaceTrait.objects.filter(
            race=self.get_object())
        return context

# view creating the races


class RaceCreateView(LoginRequiredMixin, CreateView):
    model = Race
    slug_field = 'race_slug'
    template_name = TEMPLATE_FOLDER + 'race_create_form.html'
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(RaceCreateView, self).get_context_data(**kwargs)
    #     context['race_traits'] = RaceTrait.objects.filter(
    #         race=self.get_object())
    #     return context


class RaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Race
    template_name = TEMPLATE_FOLDER + 'race_update_form.html'
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class RaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Race
    template_name = TEMPLATE_FOLDER + 'race_delete_form.html'
    success_url = reverse_lazy('race_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class RaceTraitCreateView(LoginRequiredMixin, CreateView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER + 'race_trait_create_form.html'
    fields = ['name', 'description', ]
    success_url = reverse_lazy('race_view')

    def form_valid(self, form):
        form.instance.race = get_object_or_404(Race, pk=self.kwargs['pk'])
        return super().form_valid(form)


class RaceTraitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER + 'race_trait_delete_form.html'
    success_url = reverse_lazy('race_view')
    context_object_name = 'race_trait'

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.race.author:
            return True

        return False


class RaceTraitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER + 'race_trait_update_form.html'
    fields = ['name', 'description', ]
    success_url = reverse_lazy('race_view')

    def form_valid(self, form):
        form.instance.race = get_object_or_404(Race, pk=self.kwargs['rpk'])
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.race.author:
            return True

        return False
