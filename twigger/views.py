from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'twigger/home.html', context)

# class based view with same functionality as home view
class PostListView(ListView):
    model = Post 
    template_name = 'twigger/home.html'  # <app>/<model>_<viewtype>.html  this is django convention
    # we named our template differently so we need to set this variable
    context_object_name = 'posts' # by default it is called objectList, we have diffrent name so we need to set it here
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'twigger/about.html', {'title': 'About Twigger'})