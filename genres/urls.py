from django.urls import path
from genres.views import GenreListCreateView, genre_detail_view

urlpatterns = [
    path('', GenreListCreateView.as_view(), name='genre-create-list'),
    path('/<int:pk>/', genre_detail_view, name='genre-detail-view'),
]