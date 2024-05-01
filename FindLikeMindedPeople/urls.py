from django.contrib import admin
from django.urls import path
from Landing import views as landing
from main import views as main
from Userprofile import views as user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing.landing, name='landing'),
    path('main', main.main_page, name='landing'),
    path('profile/<str:username>', user_profile.profile, name='profile'),
    path('auth/login', user_profile.authorize, name='authorize'),
    path('auth/register', user_profile.register_user, name='register'),
]

handler404 = 'Landing.views.handler404'
# handler500 = 'Landing.views.handler500'
