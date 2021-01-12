from django.urls import path
from .views import index_movie, upload_movie, update_movie, delete_movie

urlpatterns = [
    path('', index_movie, name='index_movie'),
    path('new', upload_movie, name='upload_movie'),
    path('update/<int:id>/', update_movie, name='update_movie'),
    path('delete/<int:id>/', delete_movie, name='delete_movie')
]
