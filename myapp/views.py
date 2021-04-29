from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models
from . import forms


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


class AppUserListView(generic.ListView):
    model = models.AppUser
    form_class = forms.AppUserForm


class AppUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.AppUser
    form_class = forms.AppUserForm
