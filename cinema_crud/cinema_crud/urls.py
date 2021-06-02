"""cinema_crud URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('generalpage.urls')),
    path('movie/', include('movie.urls')),
    path('branch/', include('branch.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('screening/', include('screening.urls')),
    path('seat/', include('seat.urls')),
    path('jonestaticapp/', include('jonestaticapp.urls')),
    path('user_information/', include('user_information.urls')),
    path('movie_shots/', include('movie_shots.urls')),
    path('account/', include('account.urls')),
    path('register_mpei/', include('register_mpei.urls')),
    path('admin_login/', include('admin_login.urls')),
    path('news/', include('news.urls')),
    path('branch_shots/', include('branch_shots.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
