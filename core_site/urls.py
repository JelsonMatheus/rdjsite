from django.urls import path

from . import views


urlpatterns = [
    path('', views.ForumPageView.as_view(), name='forum_page'),
]