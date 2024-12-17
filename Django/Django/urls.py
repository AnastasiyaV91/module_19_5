"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task1.views import plat, games, cart, menu, games
#from UrbanDjango.task2.views import index_func, index_class
from task1.views import sign_up_by_django, sign_up_by_html, news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', plat),
    path('platform/games/', games),
    path('platform/cart/', cart),
    path('platform/games/cart', cart),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
    path('platform/news/', news),
]

