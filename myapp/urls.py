from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Route", api.RouteViewSet)
router.register("AppUser", api.AppUserViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("myapp/Route/", views.RouteListView.as_view(), name="myapp_Route_list"),
    path("myapp/Route/create/", views.RouteCreateView.as_view(),
         name="myapp_Route_create"),
    path("myapp/Route/detail/<int:pk>/",
         views.RouteDetailView.as_view(), name="myapp_Route_detail"),
    path("myapp/Route/update/<int:pk>/",
         views.RouteUpdateView.as_view(), name="myapp_Route_update"),
    path("myapp/AppUser/", views.AppUserListView.as_view(),
         name="myapp_AppUser_list"),
    path("myapp/AppUser/detail/<int:pk>/",
         views.AppUserDetailView.as_view(), name="myapp_AppUser_detail"),
)
