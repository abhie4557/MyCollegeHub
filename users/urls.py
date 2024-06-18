from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.uploaded_documents, name='uploaded_documents'),
    path('delete/<str:document_id>/', views.delete_document, name='delete_document'),
]
