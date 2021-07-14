from django.urls import path
from .views import *

urlpatterns = [
    # C R E A T E   T O U R
    path("new", TourCreateView.as_view(), name="new_tour"),

    # A L L   T O U R S
    path('', TourListView.as_view(), name='all_tours'),

    # O N E   T O U R
    path('<int:pk>/', TourDetailView.as_view(), name='one_tour'),

    # E D I T  T O U R
    path('<int:pk>/edit', TourUpdateView.as_view(), name='edit_tour'),

    # D E L E T E   T O U R
    path('<int:pk>/delete', TourDeleteView.as_view(), name='delete_tour'),


    # A D D   L E G
    path("<int:pk>/add-leg", add_leg, name="add_leg"),
]
