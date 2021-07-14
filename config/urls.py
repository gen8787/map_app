"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include  # <---- A D D   I N C L U D E

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),  # <---- A D D
    path('accounts/', include('django.contrib.auth.urls')),  # <---- A D D

    path('articles/', include('articles.urls')),  # <---- A D D

    path('tours/', include('tours.urls')),  # <---- A D D

    path('', include('pages.urls')),  # <---- A D D   P A T T E R N S
]
