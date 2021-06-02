
from django.urls import path
from .views import index_person, upload_person, update_person, delete_person


urlpatterns = [
    path('', index_person, name='index_person'),
    path('upload/', upload_person, name='upload_person'),
    path('update/<int:id>/', update_person, name="update_person"),
    path('delete/<int:id>/', delete_person, name="delete_person"),
]