from django.shortcuts import render, redirect

from bike.models import Bike


# Create your views here.
def get_bike(request, id):
    bike = Bike.objects.filter(id=id).first()
    bike.status = True
    bike.save()
    return redirect('bike:bike-list')

def revert_bike(request, id):
    bike = Bike.objects.filter(id=id).first()
    bike.status = False
    bike.save()
    return redirect('bike:bike-list')
