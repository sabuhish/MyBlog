from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

posts = [
    {
        "author": "sabuhi",
        "title": "Blog Post 1",
        "content": "first post content",
        "data_posted": "august 27, 2018"
    },
    {
        "author": "ferid",
        "title": "Blog Post 2",
        "content": "second post content",
        "data_posted": "august 28, 2018"
    }
]

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListVeiw(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<veiwtype>.html
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 10
    
class UserPostListVeiw(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<veiwtype>.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user =get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")
class PostDetailVeiw(DetailView):
    model = Post
    
class PostCreateVeiw(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  
    def test_func(self):
        post =self.get_object()
        if self.request.user ==post.author:
            return True
        return False
        
class PostUpdateVeiw(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class PostDeleteVeiw(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  
    #this in the up will sende to home page
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
def about(request):
    return render(request, "blog/about.html", {"title": "about"})


def test(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/test.html",context)