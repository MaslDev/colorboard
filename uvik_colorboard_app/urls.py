from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.home, name='home'),
    path('play/', views.play, name='play'),
    path('history/', views.history, name='history'),
]
