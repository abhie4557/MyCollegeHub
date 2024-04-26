from django.urls import path
from . import views

urlpatterns = [
    #  path('postComment', views.postComment, name="postComment"),
    path('', views.index, name="DiscussionHome"),
    path('<str:slug>', views.discussion, name="discussion"),
]
