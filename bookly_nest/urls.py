from django.urls import path
from . import views

app_name = 'bookly_nest'

urlpatterns = [
    path('', views.index, name="index")
]
