from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="resouceshome"),

     path('pdf/<int:pdf_id>/', views.pdf_view3, name='pdf_view'),

    # path for canvas pdf.js
    # path('pdf/<str:pdf_filename>/', views.pdf_canvas_view, name='pdf_canvas_view'),


]
