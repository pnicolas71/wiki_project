from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search_entry, name="search_entry"),
    path("wiki/<str:name>", views.show_entry, name="show_entry"),

    #path("create", views.create_page, name="create_page"),
    #path("search", views.search_page, name="search_page"),
    # path("random", views.random_page, name="random_page"),
]
