from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib import admin
from django import forms
from django.contrib.auth import get_user_model
from .forms import AppUserForm
from . import models


class RouteAdminForm(forms.ModelForm):

    class Meta:
        model = models.Route
        fields = "__all__"


class RouteAdmin(admin.ModelAdmin):
    form = RouteAdminForm
    list_display = [
        "name",
        "file",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "created_by",
    ]


class AppUserAdminForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.AppUser


class AppUserAdmin(UserAdmin):
    form = AppUserForm
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'first_name',
                           'last_name', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('username', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username', )
    filter_horizontal = ()


admin.site.register(models.Route, RouteAdmin)
admin.site.register(models.AppUser, AppUserAdmin)
