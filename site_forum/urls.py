from django.urls import path

from . import views


urlpatterns = [
    path('', views.redirect_to_forum_view, name='forum_index'),
    path('accounts/logout/', views.logout_view, name='forum_logout'),

    path('foruns/<slug:slug>/', views.TopicoListView.as_view(), name='forum_page'),
    path('foruns/<slug:slug>/<int:topico_id>/', views.TopicoListView.as_view(), name='forum_topico'),
]