from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('authorized/', views.authorized, name='authorized'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('userLogin/<int:id>', views.UserLogin, name='UserLogin'),
    path('calculator/', views.Calculator, name = 'calculator'),
]
