from django.urls import path
from .import views


urlpatterns = [
    path('', views.index_movie, name='index_movie'),
    path('upload/', views.upload_movie, name='upload_movie'),
    path('update/<int:movie_id>/', views.update_movie),
    path('delete/<int:movie_id>/', views.delete_movie)
]
