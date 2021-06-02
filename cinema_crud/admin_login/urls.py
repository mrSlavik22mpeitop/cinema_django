from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^login/$', views.admin_login, name='admin_login'),
]