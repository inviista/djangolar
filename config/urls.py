from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.welcome, name="welcome"),
    path("users/", views.users_list, name="users"),
    path('city_time/', views.city_time, name='city_time'),
    path("cnt/", views.counter, name="counter"),
    path("", include("education.urls")),
]