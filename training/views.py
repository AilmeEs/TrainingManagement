from .models import Profile, Post
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView


# Create your views here.
def index(request):
<<<<<<< HEAD
    return render(request,'training/index.html')


=======
    posts = Profile.objects.all()
    return render(request, 'training/index.html', {'posts': posts})


def po_list(request, id):
    cat = Post.objects.get(id=id)
    return render(request, 'training/po_list.html', {'cat': cat})
    return render(request, 'training/index.html')


# class PostList(ListView):
#     model = Post
#     template_name = 'training/post_list.html'


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post_list')


class PostDetail(DetailView):
    model = Post
    template_name = 'training/post_detail.html'
>>>>>>> 85977112aeca8e849c6085115b34d8d2da82b330
