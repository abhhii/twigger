from django.urls import path

from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    # path('', views.home, name='twigger-home'),
    path('', PostListView.as_view(), name='twigger-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name = 'twigger-about')
    #path('about', views.about, name = 'twigger-about')
]
