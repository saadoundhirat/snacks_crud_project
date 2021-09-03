from django.shortcuts import render
from django.views.generic import (
    TemplateView ,
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)

# Create your views here.
from .models import Snack
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class SnackListView(DetailView):
    template_name = 'snacklistview.html'
    model = Snack
    context_object_name = 'snack'
class SnackDetailView(ListView):
    template_name = 'snackdetailview.html'
    model = Snack
    context_object_name = 'snack'
class SnackCreateView(CreateView):
    template_name = 'snackscreateview.html'
    model = Snack
    context_object_name = 'snack'

class SnackUpdateView(UpdateView):
    template_name = 'snacksupdateview.html'
    model = Snack

class SnackDeleteView(DeleteView):
    template_name = 'snacksdeleteview.html'
    model = Snack