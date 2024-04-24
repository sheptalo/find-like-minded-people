from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def profile(request, username=None):
    try:
        user = User.objects.get(username=username)
    except:
        user = None

    if username:
        if user:
            return HttpResponse("username: {username}".format(username=username))
    return HttpResponse("None")


def authorize(request, _type):
    user = request.user

    if (_type == 'login' or _type == 'register') and request.method == 'GET':
        return render(request, 'User/authorize.html', {'tab': _type, 'user': str(user), 'error': '0'})
    # elif request.method == 'POST' and request.user.is_anonymous:
    #     user = authenticate(username=request.POST['username'], password=request.POST['password'])
    #     if user:
    #         login(request, user)
    #         return HttpResponseRedirect('/')
    #     return render(request, 'User/authorize.html', {
    #         'tab': _type,
    #         'user': str(user),
    #         'error': 'Неправильный пароль или имя',
    #     })
    else:
        return HttpResponseRedirect('/')


def logout_func(request):
    logout(request)
