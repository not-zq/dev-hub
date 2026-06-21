from django.urls import path
from .views import home, get_top_songs

urlpatterns = [
    path("", home),
    path("getTopSongs/", get_top_songs),
]