from django.contrib import admin
from django.urls import path
from Landing import views as landing
from main import views as main
from Userprofile import views as user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing.landing, name='Like minded'),
    path('main', main.main_page, name='Главная'),
    path('user/<str:username>', user_profile.profile, name='Профиль'),
    path('auth/login', user_profile.authorize, name='Войти'),
    path('auth/register', user_profile.register_user, name='Зарегистрироваться'),
    path('find/<int:_id>', main.post_page),
    path('error/', main.error, name='Страница не найдена'),
    path('write/', main.error, name='новый пост'),
    path('search/', main.find_post, name='Поисковик'),
]

handler404 = 'Landing.views.handler404'
# handler500 = 'Landing.views.handler500'
