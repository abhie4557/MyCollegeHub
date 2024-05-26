from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="resouceshome"),
    path('filterpage', views.filter, name="filterpage"),
    
    path('filter/', views.filtered_data, name="filter"),
]
