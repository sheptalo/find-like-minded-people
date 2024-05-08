from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Post


def main_page(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, 'main_page.html', {'objects': post, 'reg': request.user.username})


def post_page(request, _id):
    try:
        post = Post.objects.get(id=_id)
        return render(request, 'post_page.html', {'Post': post, 'reg': request.user.username})
    except:
        return redirect('/error')
    pass


def error(request):
    return HttpResponse('page not found')


def parameters(request):
    params = {}
    link = request.build_absolute_uri()
    try:
        param = link.split('?')[1]
        for query_string in param.split('&'):
            name, key = query_string.split('=')
            params[name] = key
    except:
        pass
    return params


def find_post(request):
    err = ''

    if request.method == 'POST':

        search = request.POST.get('text')
        posts = Post.objects.filter(title__icontains=search).order_by('-created_at')

        if posts.count() == 0:
            posts = Post.objects.all().order_by('-created_at')
            err = 'None'

        return render(request, 'search.html', {'objects': posts,
                                               'reg': request.user.username,
                                               'err': err,
                                               'last': search})

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'search.html', {'objects': posts, 'reg': request.user.username, 'err': err})


