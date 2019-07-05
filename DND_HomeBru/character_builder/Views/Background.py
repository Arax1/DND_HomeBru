from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from character_builder.models import Background
TEMPLATE_FOLDER = 'character_builder/'


class BackgroundListView(ListView):
    model = Background
    template_name = TEMPLATE_FOLDER + 'background_list.html'
    context_object_name = "backgrounds"


class BackgroundDetailView(DetailView):
    model = Background
    context_object_name = "background_details"
    template_name = TEMPLATE_FOLDER + 'background_detail.html'


class BackgroundCreateView(LoginRequiredMixin, CreateView):
    model = Background
    template_name = TEMPLATE_FOLDER + 'background_create_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BackgroundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Background
    template_name = TEMPLATE_FOLDER + 'background_update_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class BackgroundDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Background
    template_name = TEMPLATE_FOLDER + 'background_delete_form.html'
    success_url = reverse_lazy('background_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False
