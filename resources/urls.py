from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="resouceshome"),
    path('pdf/<str:pdf_cat>/', views.findpdf, name="pdf_cat"),
    path('pdf_view', views.findpdf, name="url"),


    path('pdf-view/<int:pdf_id>/', views.pdf_view, name='pdf_view'),

    # path for canvas pdf.js
    # path('pdf/<str:pdf_filename>/', views.pdf_canvas_view, name='pdf_canvas_view'),
 

]
