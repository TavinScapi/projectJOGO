from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('menu/', views.menu, name='menu'),
    path('cameras/', views.cameras, name='cameras'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('sair/', views.sair, name='sair'),
    path('identificacao/', views.identificacao, name='identificacao'),
    path('bestiario/', views.bestiario, name='bestiario'),
    path('cutscene/', views.cutscene, name='cutscene'),
    path('JOGO/<str:parte>/', views.JOGO, name='JOGO'),
    path('creditos/', views.creditos, name='creditos'),
    path('splash_screen/', views.splash_screen, name='splash_screen'),
    path('room/', views.room, name='room'),

]
