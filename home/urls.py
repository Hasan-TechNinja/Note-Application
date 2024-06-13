from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('authorized/', views.authorized, name='authorized'),
    path('userLogin/', views.userLogin, name='userLogin'),
]
