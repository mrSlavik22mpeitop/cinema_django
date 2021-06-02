from django.urls import path
from .views import index_news, upload_news, update_news, delete_news

urlpatterns = [
    path('', index_news, name='index_news'),
    path('upload/', upload_news, name='upload_news'),
    path('update/<int:id>/', update_news, name="update_news"),
    path('delete/<int:id>/', delete_news, name="delete_news")
]
