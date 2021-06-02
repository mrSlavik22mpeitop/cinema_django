from django.urls import path
from .views import index_screening, upload_screening, update_screening, delete_screening

urlpatterns = [
    path('', index_screening, name='index_screening'),
    path('upload/', upload_screening, name='upload_screening'),
    path('update/<int:id>/', update_screening, name="update_screening"),
    path('delete/<int:id>/', delete_screening, name="delete_screening")
]
