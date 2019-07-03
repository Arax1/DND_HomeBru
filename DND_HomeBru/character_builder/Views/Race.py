from . import *

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
