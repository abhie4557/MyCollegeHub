from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="resouceshome"),
    
    path('BCA', views.index, name="bca"),
    path('BBA', views.index, name="bba"),
    path('BHM', views.index, name="bhm"),
    
    path('BCA/<str:type>', views.bcadocs, name="BCAdocs"),
    path('BBA/<str:type>', views.bbadocs, name="BBAdocs"),
    path('BHM/<str:type>', views.bhmdocs, name="BHMdocs"),
    
    path('filterpage', views.filter, name="filterpage"),
    
    path('filter/', views.filtered_data, name="filter"),
]
