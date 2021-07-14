from django.urls import path
from .views import *

urlpatterns = [
    # C R E A T E
    path("new", ArticleCreateView.as_view(), name="new_article"),

    # A L L   A R T I C L E S
    path('', ArticleListView.as_view(), name='all_articles'),

    # O N E   A R T I C L E
    path('<int:pk>/', ArticleDetailView.as_view(), name='one_article'),

    # E D I T  A R T I C L E
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='edit_article'),

    # D E L E T E   A R T I C L E
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete_article'),
]
