from django.urls import path
from .views import index_branch_shots, upload_branch_shots, update_branch_shots, delete_branch_shots

urlpatterns = [
    path('', index_branch_shots, name='index_branch_shots'),
    path('upload/', upload_branch_shots, name='upload_branch_shots'),
    path('update/<int:id>/', update_branch_shots, name="update_branch_shots"),
    path('delete/<int:id>/', delete_branch_shots, name="delete_branch_shots")
]
