from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("edit/", views.index, name="index"),
    path("", views.index, name="index"),
    path("search", views.search_entry, name="search_entry"),
    path("create", views.create_entry, name="create_entry"),
    path("edit/<str:name>", views.edit_entry, name="edit_entry"),
    path("random", views.show_random, name="show_random"),
    path("wiki/<str:name>", views.show_entry, name="show_entry"),

]
