from django.urls import path

from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='twigger-home'),
    path('', PostListView.as_view(), name='twigger-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/like/', PostLikeView.as_view(), name='post-liked'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name = 'twigger-about')

    #path('about', views.about, name = 'twigger-about')
]
