from django.urls import path
from genres.views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('', genre_create_list_view, name='genre-create-list'),
    path('/<int:pk>/', genre_detail_view, name='genre-detail-view'),
]