from django.shortcuts import render, redirect
from .models import  *
from bike.models import Bike


# Create your views here.
def get_bike(request, id):
    bike = Bike.objects.get(id=id)
    bike.status = True
    bike.save()

    obj = BikeToUser()
    obj.user = request.user
    obj.bike = bike
    obj.status = True
    obj.save()

    return redirect('bike:bike-list')

def revert_bike(request, id):
    bike = Bike.objects.filter(id=id).first()
    bike.status = False
    bike.save()

    obj = BikeToUser.objects.filter(bike_id=id, status=True).first()
    obj.status = False
    obj.save()

    return redirect('bike:bike-list')
