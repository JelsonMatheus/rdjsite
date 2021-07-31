from django.urls import path

from .views import views, ajax

app_name = 'forum'

urlpatterns = [
    path('', views.redirect_to_forum_view, name='index'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),

    path('foruns/<slug:slug>/topicos/', views.TopicoView.as_view(), name='list_topico'),
    path('foruns/<slug:slug>/topicos/<int:topico_id>/', views.TopicoDetailView.as_view(), name='topico'),
    path('foruns/<slug:slug>/topicos/<int:topico_id>/respostas/', views.RespostaView.as_view(), name='resposta'),
    path('foruns/<slug:slug>/topicos/<int:topico_id>/respostas/<int:resposta_id>/', views.RespostaView.as_view(), name='detail_resposta'),

    path('ajax/topico/', ajax.JSONTopicoView.as_view(), name='jax_topico'),
    path('ajax/resposta/', ajax.JSONRespostaView.as_view(), name='jax_resposta'),
]