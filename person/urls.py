from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="personHome"),
    path('add/', views.add_person, name="addPerson"),
    path('show', views.get_all_person, name="getPerson"),
]