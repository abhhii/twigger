from django.urls import path

from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # path('', views.home, name='twigger-home'),
    path('', PostListView.as_view(), name='twigger-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-'),
    path('about/', views.about, name = 'twigger-about')

    #path('about', views.about, name = 'twigger-about')
]
