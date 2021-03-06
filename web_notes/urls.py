"""web_notes URL Configuration

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
from django.urls import path
from note.views import index, auth, register, note_create, note_list
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='home'), 
    path('auth', auth, name='auth'), 
    path('register', register, name='register'), 
    path('note_create', note_create, name='note_create'), 
    path('note_list', note_list, name='note_list'), 
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
