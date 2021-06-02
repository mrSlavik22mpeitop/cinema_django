from django.urls import path
from .views import index_seat, upload_seat, update_seat, delete_seat

urlpatterns = [
    path('', index_seat, name='index_seat'),
    path('upload/', upload_seat, name='upload_seat'),
    path('update/<int:id>/', update_seat, name="update_seat"),
    path('delete/<int:id>/', delete_seat, name="delete_seat")
]
