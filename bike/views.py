from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.

class ListBikeView(ListView):
    template_name = 'bike_list.html'
    context_object_name = 'bike'
    queryset = Bike.objects.all()

