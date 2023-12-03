from django.shortcuts import render, redirect
from .models import *
from reservation.models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListBikeView(ListView):
    template_name = 'bike_list.html'
    context_object_name = 'bike'
    queryset = Bike.objects.all()
    ordering = ['status']

login_url = "/login/"
class MyBikesView(LoginRequiredMixin ,ListView):
    login_url = "/account/login"
    template_name = 'my_bike.html'
    queryset = BikeToUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bike"] = BikeToUser.objects.filter(user=self.request.user, status=True).all()
        return context
