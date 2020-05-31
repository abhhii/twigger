from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='twigger-home'),
    path('about/', views.about, name = 'twigger-about')
    #path('about', views.about, name = 'twigger-about')
]
