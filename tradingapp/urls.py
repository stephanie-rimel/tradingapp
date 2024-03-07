"""tradingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from tradingapp_api import urls as trading_urls, views
from tradingapp import urls as urls


urlpatterns = [
    # path('', include(urls)),
    path ('', views.index, name='home'),
    path ('about', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('trading/', include(trading_urls)),
]