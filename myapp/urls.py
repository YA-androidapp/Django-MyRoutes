from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Route", api.RouteViewSet)
router.register("AppUser", api.AppUserViewSet)
router.register("Image", api.ImageViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("route/", views.RouteListView.as_view(), name="myapp_Route_list"),
    path("route/create/", views.RouteCreateView.as_view(),
         name="myapp_Route_create"),
    path("route/detail/<int:pk>/",
         views.RouteDetailView.as_view(), name="myapp_Route_detail"),
    path("route/update/<int:pk>/",
         views.RouteUpdateView.as_view(), name="myapp_Route_update"),
    path('route/delete/<int:pk>/', views.RouteDeleteView.as_view(), name='myapp_Route_delete'),
    path("route/upload/",
         views.RouteMultiUploadView.as_view(), name="myapp_Route_upload"),
    path("user/", views.AppUserListView.as_view(),
         name="myapp_AppUser_list"),
    path("user/detail/<int:pk>/",
         views.AppUserDetailView.as_view(), name="myapp_AppUser_detail"),
    path("image/", views.ImageListView.as_view(), name="myapp_Image_list"),
    path("image/create/", views.ImageCreateView.as_view(), name="myapp_Image_create"),
    path("image/detail/<int:pk>/", views.ImageDetailView.as_view(), name="myapp_Image_detail"),
    path("image/update/<int:pk>/", views.ImageUpdateView.as_view(), name="myapp_Image_update"),
]
