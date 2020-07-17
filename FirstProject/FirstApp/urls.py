"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , include

from FirstApp import views

urlpatterns = [
    path('' , views.index.as_view()),
    path('contact/' , views.contact.as_view()),
    path('home/' , views.home),
    path('signup/' , views.signup ),
    path('messages/' , views.AllMessages.as_view() ),
    path('message/<int:pk>' , views.datail.as_view() , name = 'detail'),
    path('message/' , views.SendMessage.as_view() ),
]
