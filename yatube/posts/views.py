from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Group, Post, User

PAGE_NUM = 10


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, PAGE_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, PAGE_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = User.objects.get(username=username)
    post_list = Post.objects.filter(author=author)
    posts_number = post_list.count()
    paginator = Paginator(post_list, PAGE_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'posts_number': posts_number,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    posts = Post.objects.get(id=post_id)
    posts_numbers = Post.objects.count()
    context = {
        'posts': posts,
        'posts_numbers': posts_numbers,
    }
    return render(request, 'posts/post_detail.html', context)

