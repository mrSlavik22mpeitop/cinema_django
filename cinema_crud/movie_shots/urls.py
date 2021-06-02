from django.urls import path
from .views import index_movie_shots, upload_movie_shots, update_movie_shots, delete_movie_shots

urlpatterns = [
    path('', index_movie_shots, name='index_movie_shots'),
    path('upload/', upload_movie_shots, name='upload_movie_shots'),
    path('update/<int:id>/', update_movie_shots, name="update_movie_shots"),
    path('delete/<int:id>/', delete_movie_shots, name="delete_movie_shots")
]
