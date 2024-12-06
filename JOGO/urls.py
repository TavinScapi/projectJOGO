from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('menu/', views.menu, name='menu'),
    path('carregar/', views.carregar_jogo, name='carregar_jogo'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('sair/', views.sair, name='sair'),

    path('identificacao/', views.identificacao, name='identificacao'),
    path('JOGO/<str:parte>/', views.JOGO, name='JOGO'),
    path('creditos/', views.creditos, name='creditos'),


]
