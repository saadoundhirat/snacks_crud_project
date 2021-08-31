from django.urls import path

# import the views
from .views import HomePageView

# path is a function the django framework provides to help with url routing and takes a path and a view then use as_view to convert it to a view

urlpatterns = [
    path('/', HomePageView.as_view(), name='home'),
]