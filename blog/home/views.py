from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

def index(request):
    return render(request, 'home/index.html')


def showpost(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home/home.html', context)

class PostCreateView(CreateView):
    template_name = 'home/create.html'
    form_class = PostForm
    success_url = reverse_lazy('showpost')
