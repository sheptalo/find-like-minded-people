from django.contrib import admin
from django.urls import path
from Landing import views as landing
from Userprofile import views as user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing.landing, name='landing'),
    path('profile/<str:username>', user_profile.profile, name='profile'),
    path('auth/<str:_type>', user_profile.authorize, name='authorize'),
]

handler404 = 'Landing.views.handler404'
# handler500 = 'Landing.views.handler500'
