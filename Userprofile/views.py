from django.contrib.auth.models import User
from django.http import HttpResponse
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


def login(request):
    pass


def logout(request):
    pass


def register(request):
    pass
