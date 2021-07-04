from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
import os

import hashlib
from datetime import datetime


class RouteListView(generic.ListView):
    model = models.Route
    form_class = forms.RouteForm


class RouteCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Route
    form_class = forms.RouteForm

    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super(RouteCreateView, self).form_valid(form)


class RouteDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Route
    form_class = forms.RouteForm


class RouteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Route
    form_class = forms.RouteForm
    pk_url_kwarg = "pk"


class RouteDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    model = models.Route
    success_url = reverse_lazy('myapp_Route_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


def custom_upload_to(filename):
    current_time = datetime.now()
    pre_hash_name = os.path.basename(filename)
    extension = str(filename).split('.')[-1]
    hs_filename = '{}.{}'.format(hashlib.md5(pre_hash_name.encode()).hexdigest(), extension)
    print('pre_hash_name, hs_filename', pre_hash_name, hs_filename)
    saved_path = 'upload/files/'
    return '{}{}'.format(saved_path, hs_filename)


class RouteMultiUploadView(LoginRequiredMixin, generic.FormView):
    form_class = forms.RouteMultipleUploadForm
    template_name = 'myapp/routes_upload.html'
    success_url = reverse_lazy('myapp_Route_list')

    def form_valid(self, form):
        file_list = form.save()
        name = form.data.get('name')
        for file in file_list:
            filestem = os.path.splitext(os.path.basename(file))[0]
            models.Route.objects.create(name = name + ' ' + filestem, file = custom_upload_to(file), created_by_id = self.request.user.id)
        return super().form_valid(form)


class AppUserListView(generic.ListView):
    model = models.AppUser
    form_class = forms.AppUserForm


class AppUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.AppUser
    form_class = forms.AppUserForm

class ImageListView(generic.ListView):
    model = models.Image
    form_class = forms.ImageForm


class ImageCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Image
    form_class = forms.ImageForm

    def get_context_data(self, **kwargs):
        print(self.get_template_names())
        context = super(ImageCreateView, self).get_context_data(**kwargs)
        context['routes'] = models.Route.objects.all()
        return context

    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super(ImageCreateView, self).form_valid(form)


class ImageDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Image
    form_class = forms.ImageForm


class ImageUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Image
    form_class = forms.ImageForm
    pk_url_kwarg = "pk"
