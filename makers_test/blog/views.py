from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Post, Category


def categories_list(request):
    """

    :param request:
    :return:
    """
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  {'categories_list': categories})


def posts_list(request):
    category = request.GET.get('category')
    posts = Post.objects.filter(category_id=category)
    print(posts.query)
    # posts = Post.objects.filter(category__slug=category) -> chtoby obratitsya k lubomu polu
    return render(request, 'blog/posts_list.html', {'posts': posts})


def post_details(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post_details.html', {'post': post})


def add_post(request):
    return render(request, 'blog/add_post.html', {})


def update_post(request, pk):
    return render(request, 'blog/update_post.html', {})


def delete_post(request, pk):
    return render(request, 'blog/delete_post.html', {})
