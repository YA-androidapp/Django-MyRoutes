from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic


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


class RouteDeleteView(generic.edit.DeleteView):
    model = models.Route
    success_url = reverse_lazy('myapp_Route_list')


class AppUserListView(generic.ListView):
    model = models.AppUser
    form_class = forms.AppUserForm


class AppUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.AppUser
    form_class = forms.AppUserForm
