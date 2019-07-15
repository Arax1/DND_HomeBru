from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from character_builder.models import Background, BackgroundTrait
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



class BackgroundTraitCreateView(LoginRequiredMixin, CreateView):
    model = BackgroundTrait
    template_name = TEMPLATE_FOLDER + 'background_trait_create_form.html'
    fields = ['name', 'description', ]

    def get_context_data(self, **kwargs):
        context = super(BackgroundTraitCreateView, self).get_context_data(**kwargs)
        context['pkey'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.background = get_object_or_404(Background, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('background_detail', kwargs={'pk': self.kwargs['pk']})




class BackgroundTraitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BackgroundTrait
    template_name = TEMPLATE_FOLDER + 'background_trait_delete_form.html'
    success_url = reverse_lazy('background_view')
    context_object_name = 'background_trait'

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.background.author:
            return True

        return False

    def get_success_url(self):
        object = self.get_object()
        return reverse('background_detail', kwargs={'pk': object.background.id})


class BackgroundTraitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BackgroundTrait
    template_name = TEMPLATE_FOLDER + 'background_trait_update_form.html'
    fields = ['name', 'description', ]
    success_url = reverse_lazy('background_view')

    def get_context_data(self, **kwargs):
        context = super(BackgroundTraitUpdateView, self).get_context_data(**kwargs)
        context['pkey'] = self.kwargs['rpk']
        return context

    def form_valid(self, form):
        form.instance.background = get_object_or_404(Background, pk=self.kwargs['rpk'])
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.background.author:
            return True

        return False

    def get_success_url(self):
        object = self.get_object()

        return reverse('background_detail', kwargs={'pk': object.background.id})
