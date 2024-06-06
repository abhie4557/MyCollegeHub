from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="DiscussionHome"),
     path('postComment', views.DiscussionComment, name="postComment"),
    path('<str:slug>', views.discussion, name="discussion"),
]
