from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Post


def main_page(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, 'main_page.html', {'objects': post})


def post_page(request, _id):
    try:
        post = Post.objects.get(id=_id)
        return render(request, 'post_page.html', {'Post': post})
    except:
        return redirect('/error')
    pass


def error(request):
    return HttpResponse('page not found')
