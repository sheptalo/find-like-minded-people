from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from Userprofile.forms import LoginForm
from Userprofile.models import UserProfileModel


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

    if (_type == 'login' or _type == 'register') and request.method == 'GET' and request.user.is_anonymous:
        return render(request, 'User/authorize.html', {'tab': _type, 'user': str(user), 'form': LoginForm()})
    elif request.method == 'POST' and request.user.is_anonymous:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_login = authenticate(username=username, password=password)
            if user_login:
                login(request, user_login)
                return HttpResponseRedirect('/')  # TODO заменить на главную страницу вместо лендинга
            else:
                form.add_error(None, 'Неправильное имя или пароль')
                return render(request, 'User/authorize.html', {'form': form,
                                                               'tab': 'login',
                                                               'user': str(user)})
        else:
            return render(request, 'User/authorize.html', {'form': form,
                                                           'tab': 'login',
                                                           'user': str(user)})
    else:
        return HttpResponseRedirect('/')  # TODO redirect('main')


def register_user(request):  # TODO сделать другую форму и проверять есть ли пользователь с таким ником
    if request.method == 'POST' and request.user.is_anonymous:
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'],
                                        email=request.POST['email']
                                        )
        UserProfileModel.objects.create(user_main=user)
        redirect('/auth/login')
    return redirect('/auth/login')


def logout_func(request):
    logout(request)
