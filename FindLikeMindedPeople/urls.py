from django.contrib import admin
from django.urls import path
from Landing import views as landing


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing.landing, name='landing')
]
