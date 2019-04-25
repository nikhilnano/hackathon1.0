"""abcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chat_app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/', views.home_view, name='home'),
    path('home/', views.home),
    path('register/home/', views.chat),
    path('', views.register,name='register'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
path('hi/', views.show_chat,name='hi'),      
path('shw/', views.add_chat1,name='shw'),
path('chat/', views.show_chats,name='chat'),
]