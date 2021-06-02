from django.urls import path
from . import views
from .views import index_branch, upload_branch, update_branch, delete_branch

urlpatterns = [
    path('', index_branch, name='index_branch'),
    path('upload/', upload_branch, name='upload_branch'),
    path('update/<int:id>/', update_branch, name="update_branch"),
    path('delete/<int:id>/', delete_branch, name="delete_branch"),
]