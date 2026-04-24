from django.urls import path

from .views import event_create, event_list

urlpatterns = [
    path("", event_list, name="event_list"),
    path("novo/", event_create, name="event_create"),
]
