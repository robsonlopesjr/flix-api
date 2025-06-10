from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('', GenreListCreateView.as_view(), name='genre-create-list'),
    path('/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]