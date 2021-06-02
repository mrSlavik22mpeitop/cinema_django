from django.urls import path
from .import views
urlpatterns = [
    path('jonepages/', views.index_john, name = 'jonepages'),
    # path('', views.now_screening, name = 'now_screening')
]