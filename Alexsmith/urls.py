"""
URL configuration for Alexsmith project.

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
from frontend.views import *
from about.views import *
from contact.views import *
from skills.views import *
from portfolio.views import *
from services.views import *
urlpatterns = [
    path('admin/', admin, name='admin'),
    path('', home, name='home'),
    path('about/', Aboutupdate, name='about'),
    path('contact/', Contactupdate, name='contact'),
    path('skills/', skills, name='skills'),
    path('skills/<int:id>', read, name='skillsdetail'),
    path('skills/create/', create, name='skillcreate'),
    path('portfolio/', portfolio),
    path('services/', services, name='services'),
    path('services/create/', create, name='servicescreate'),
    path('services/<int:id>', Serviceupdate, name='serviceedit'),
    path('services/destroy/<int:id>', destroy),
    
    
    
]