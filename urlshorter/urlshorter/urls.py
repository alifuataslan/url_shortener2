"""urlshorter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from accounts import views
from root import views as rootviews
# FIXME include edecegiz
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',rootviews.index,name="index"),
    path('login/',views.loginuser,name="login" ),
    path('register/',views.register,name="register" ),
    path('logout/',views.logoutuser,name="logout"),
    path('dashboard/',rootviews.dashboard,name="dashboard"),
    path('allurls/',rootviews.allurls,name="allurls"),
    path('deleteurl/<int:id>/',rootviews.delete,name="delete"),
    path('<slug:key>/',rootviews.routeurl,name="route"),
    path('activateurl/<int:id>',rootviews.activateurl,name="activate"),
    path('activate/subs/',views.activatesubs,name="subs"),
    
]
