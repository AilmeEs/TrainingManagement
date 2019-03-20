from django.shortcuts import render
from .models import Profile, Post


# Create your views here.
def index(request):
    posts = Profile.objects.all()
    return render(request, 'training/index.html', {'posts': posts})


def po_list(request, id):
    cat = Post.objects.get(id=id)
    return render(request, 'training/po_list.html', {'cat': cat})
