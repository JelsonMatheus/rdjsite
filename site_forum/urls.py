from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.redirect_to_forum_view, name='index'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),

    path('foruns/<slug:slug>/', views.TopicoListView.as_view(), name='page'),
    path('foruns/<slug:slug>/<int:topico_id>/', views.TopicoListView.as_view(), name='topico'),
]