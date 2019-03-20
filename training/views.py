
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse


# Create your views here.
def index(request):
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
    return render(request, 'training/index.html')


def register(request):
    # if request.method == "POST":
    #     form = UserCreationForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data['username']
    #         user = User.objects.get(username=username)
    #         Profile.objects.create(user=user)
    #         messages.success(request, '注册成功！')
    #         return redirect("/")
    #     else:
    #         return render(request, 'account/register.html', {'form': form})
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'account/register.html', {'form': form})
    phonenumbers = settings.AUTH_USER_MODEL.profile.phonenumber.all()
    user_phonenumber = request.GET.get(user=request.user)
    if user_phonenumber in phonenumbers:
        user_password = '123456'
        return JsonResponse({
            'user_password': user_password
        })
    else:
        return JsonResponse ({
            'message':'没有这个用户'
        })
