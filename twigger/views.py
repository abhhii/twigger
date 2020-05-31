from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'twigger/home.html', context)

def about(request):
    return render(request, 'twigger/about.html', {'title': 'About Twigger'})