from django.shortcuts import render
from .models import Post
<<<<<<< HEAD

# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts' : posts})
=======
from django.views.generic import ListView, DetailView

#def posts(request):
#    posts = Post.objects.all()
#    return render(request, 'posts.html', {'posts' : posts})

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()
>>>>>>> main
