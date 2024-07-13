"""EarthLoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from elapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('signin.html',views.signin,name='signin'),
    path('signup.html',views.signup,name='signup'),
    path('dashboard.html',views.dashboard,name='dashboard'),
    path('profile.html',views.profile,name='profile'),
    path('edit.html',views.edit,name='edit'),
    path('newpass.html',views.newpass,name='newpass'),
    path('helps.html',views.helps,name='helps'),
    path('report.html',views.report,name='report'),
    path('info.html',views.info, name='info'),
    path('vegetable.html',views.vegetable,name='vegetable'),
    path('fruits.html',views.fruits, name='fruits'),
    path('dryfruit.html',views.dryfruit, name='dryfruit'),
    path('store.html',views.store,name='store'),
    path('offers.html',views.offers,name='offers'),
]
