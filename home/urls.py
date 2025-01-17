from django.urls import path
from . import views
# from django.views.generic import TemplateView


app_name = 'home'
urlpatterns = [
    # ex: /home
    path('', views.welcome_page, name='main-page'),
    path('home/about/', views.about, name='home-about'),
    path('home/certs/', views.certs, name='home-certs'),
]
