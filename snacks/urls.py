from django.urls import path

# import the views
from .views import (
    HomePageView,
    SnackListView,
    SnackDetailView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView,
    )

# path is a function the django framework provides to help with url routing and takes a path and a view then use as_view to convert it to a view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snack/', SnackListView.as_view(), name='snack_list'),
]