from . import *

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
