"""backend URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from . import views

from signup import urls as signup_urls
from branding import urls as branding_urls
from hobnobAdmin import urls as hobnob_admin_urls

urlpatterns = [
    url(r'', include(signup_urls, namespace='signup')),
    url(r'', include(branding_urls, namespace='branding')),
    url(r'^hobnobadmin/', include(hobnob_admin_urls, namespace='hobnob_admin')),
    path('admin/', admin.site.urls),
]
