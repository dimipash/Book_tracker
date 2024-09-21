from django.urls import path
from . import views

app_name = 'bookly_nest'

urlpatterns = [
    path('', views.index, name="index"),
    path('genres/', views.genres, name="genres"),
    path('genres/<int:genre_id>', views.genre, name="genre"),
]
