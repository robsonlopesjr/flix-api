from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]