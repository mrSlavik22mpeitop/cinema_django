from django.urls import path
from .import views
from .views import index_fixation, upload_fixation, update_fixation, delete_fixation

urlpatterns = [
    path('', views.index_mpei, name='mpei'),
    path("upload_mpei", views.MoviesView.as_view()),
    path("<int:pk>", views.MovieDetailView.as_view()),
    path("upload_screening", views.MovieScreening.as_view()),
    path("mpei/<int:pk>", views.MovieDetailScreening.as_view(), name='mpei_map'),
    path("upload_news", views.NewsView.as_view()),
    path("book_seat/<int:screening_id>/", views.book_seat, name='book_seats'),
    path('index/upload/', upload_fixation, name='upload_fixation'),
    path('index/update/<int:id>/', update_fixation, name="update_fixation"),
    path('index/delete/<int:id>/', delete_fixation, name="delete_fixation"),
    path('index/', index_fixation, name='index_fixation'),
    path('user_account/', views.user_account, name='user')
]


