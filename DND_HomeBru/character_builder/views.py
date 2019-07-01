# comment
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Race, Class, Background, Character, Trait, RaceTrait
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

TEMPLATE_FOLDER = 'character_builder/'


# Create your views here.


# homepage view
def homepage(request):
    return render(request, "home.html", {'title': 'HomeBru - Home'})

# view listing all races


class RaceListView(ListView):
    model = Race
    template_name = TEMPLATE_FOLDER +'race_list.html'
    context_object_name = "races"

    # def get_context_data(self, **kwargs):
    #     context = super(RaceListView, self).get_context_data(**kwargs)
    #     context['race_traits'] = RaceTrait.objects.filter(race=self.get_object())
    #     return context

class RaceDetailView(DetailView):
    model = Race
    context_object_name = "race_details"
    template_name = TEMPLATE_FOLDER +'race_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RaceDetailView, self).get_context_data(**kwargs)
        context['race_traits'] = RaceTrait.objects.filter(race=self.get_object())
        return context

# view creating the races


class RaceCreateView(LoginRequiredMixin, CreateView):
    model = Race
    template_name = TEMPLATE_FOLDER + 'race_create_form.html'
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(RaceCreateView, self).get_context_data(**kwargs)
        context['race_traits'] = RaceTrait.objects.filter(race=self.get_object())
        return context


class RaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Race
    template_name = TEMPLATE_FOLDER +'race_update_form.html'
    fields = ['name', 'description', 'age', 'alignment', 'size', 'speed' ]

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
    template_name = TEMPLATE_FOLDER +'race_delete_form.html'
    success_url = reverse_lazy('race_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class ClassListView(ListView):
    model = Class
    template_name = TEMPLATE_FOLDER +  'class_list.html'
    context_object_name = "classes"


class ClassDetailView(DetailView):
    model = Class
    context_object_name = "class_details"
    template_name = TEMPLATE_FOLDER +'class_detail.html'


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    template_name = TEMPLATE_FOLDER + 'class_create_form.html'
    fields = ['name', 'description', 'hit_dice']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Class
    template_name = TEMPLATE_FOLDER +'class_update_form.html'
    fields = ['name', 'description', 'hit_dice']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class ClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Class
    template_name = TEMPLATE_FOLDER +'class_delete_form.html'
    success_url = reverse_lazy('class_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class BackgroundListView(ListView):
    model = Background
    template_name = TEMPLATE_FOLDER + 'background_list.html'
    context_object_name = "backgrounds"


class BackgroundDetailView(DetailView):
    model = Background
    context_object_name = "background_details"
    template_name = TEMPLATE_FOLDER +'background_detail.html'


class BackgroundCreateView(LoginRequiredMixin, CreateView):
    model = Background
    template_name = TEMPLATE_FOLDER + 'background_create_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BackgroundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Background
    template_name = TEMPLATE_FOLDER +'background_update_form.html'
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
    template_name = TEMPLATE_FOLDER +'background_delete_form.html'
    success_url = reverse_lazy('background_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class CharacterListView(ListView):
    model = Character
    template_name = TEMPLATE_FOLDER +  'character_list.html'
    context_object_name = 'characters'


class CharacterDetailView(DetailView):
    model = Character
    template_name = TEMPLATE_FOLDER +'character_detail.html'
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
    template_name = TEMPLATE_FOLDER +'character_update_form.html'
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
    template_name = TEMPLATE_FOLDER +'character_delete_form.html'
    success_url = reverse_lazy('character_view')

    def test_func(self):
        object = self.get_object()

        if self.request.user == object.author:
            return True

        return False


class TraitCreateView( CreateView):
    model = Trait
    template_name = TEMPLATE_FOLDER +'trait_create_form.html'
    fields = ['name','description']
    success_url = reverse_lazy('home')



class TraitListView(ListView):
    model  = Trait
    template_name = TEMPLATE_FOLDER + 'trait_list.html'
    context_object_name = 'traits'

class TraitDetailView(DetailView):
    model = Trait
    template_name = TEMPLATE_FOLDER + 'trait_detail.html'
    context_object_name  = 'trait_details'


class TraitDeleteView( DeleteView):
    model = Trait
    template_name = TEMPLATE_FOLDER +'trait_delete_form.html'
    success_url = reverse_lazy('home')



class TraitUpdateView( UpdateView):
    model = Trait
    template_name = TEMPLATE_FOLDER +'trait_update_form.html'
    fields = ['name','description']

class RaceTraitCreateView( CreateView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER +'race_trait_create_form.html'
    fields = ['name','description', 'race']
    success_url = reverse_lazy('home')




class RaceTraitListView(ListView):
    model  = RaceTrait
    template_name = TEMPLATE_FOLDER + 'race_trait_list.html'
    context_object_name = 'race_traits'

class RaceTraitDetailView(DetailView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER + 'race_trait_detail.html'
    context_object_name  = 'race_trait_details'


class RaceTraitDeleteView( DeleteView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER +'race_trait_delete_form.html'
    success_url = reverse_lazy('home')
    context_object_name = 'race_trait'



class RaceTraitUpdateView( UpdateView):
    model = RaceTrait
    template_name = TEMPLATE_FOLDER +'race_trait_update_form.html'
    fields = ['name','description', 'race']
