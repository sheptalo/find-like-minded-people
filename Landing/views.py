from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def landing(request):
    return render(request, 'index.html')


def handler404(request, exception):
    return HttpResponseRedirect('/')
