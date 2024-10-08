from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from Userprofile.forms import LoginForm, RegisterForm
from Userprofile.models import UserProfileModel
from main.models import Post


# Create your views here.
def profile(request, username=None):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user)
    except:
        user = None

    if not username or not user:
        return HttpResponse("None")
    return HttpResponse(f"username: {username}")


def authorize(request):
    user = request.user
    print(user.id)
    if request.method == 'GET' and request.user.is_anonymous:
        return render(request, 'User/authorize.html', {'tab': 'login',
                                                       'user': str(user),
                                                       'form': LoginForm(),
                                                       'reg': request.user.username})
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
                                                               'user': str(user),
                                                               'reg': request.user.username})

        else:
            return render(request, 'User/authorize.html', {'form': form,
                                                           'tab': 'login',
                                                           'user': str(user),
                                                           'reg': request.user.username})

    else:
        return HttpResponseRedirect(f'/user/{request.user.username}')  # TODO redirect('main')


def logout_func(request):
    logout(request)
    return redirect('/auth/login')


def register_user(request):
    user = request.user
    if request.method == 'GET' and request.user.is_anonymous:
        return render(request, 'User/authorize.html', {'tab': 'register',
                                                       'user': str(user),
                                                       'form': RegisterForm(),
                                                       'reg': request.user.username})

    if request.method == 'POST' and request.user.is_anonymous:

        form = RegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                name_user = User.objects.get(username=username)
            except:
                name_user = None

            try:
                email_user = User.objects.get(email=email)
            except:
                email_user = None

            if name_user:
                form.add_error(None, 'Пользователь с таким именем уже зарегистрирован, выберите другое.')
                return render(request, 'User/authorize.html',
                              {'tab': 'register',
                               'user': str(user),
                               'form': form,
                               'reg': request.user.username})
            elif email_user:
                form.add_error(None, 'На эту почту зарегистрирован аккаунт Войти?')
                return render(request, 'User/authorize.html',
                              {'tab': 'register',
                               'user': str(user),
                               'form': form,
                               'reg': request.user.username})

            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email
                                            )

            UserProfileModel.objects.create(user_main=user)

            redirect('/auth/login')
    return redirect('/auth/login')
