from django.shortcuts import render, redirect
from .models import *
from bike.models import Bike
from reservation.models import *
from django.contrib import messages


# Create your views here.
def get_bike(request, id):
    conter = BikeToUser.objects.filter(user=request.user, status=True).count()
    if conter < 3:
        bike = Bike.objects.get(id=id)
        bike.status = True
        bike.save()

        obj = BikeToUser()
        obj.user = request.user
        obj.bike = bike
        obj.status = True
        obj.save()
        return redirect('bike:bike-list')
    else:
        messages.error(request, 'شما به حد مجاز اجاره رسیده اید! ابتدا یک دوچرخه را بازگردانید')
        return redirect("bike:my-bike")


def revert_bike(request, id):
    bike = Bike.objects.filter(id=id).first()
    bike.status = False
    bike.save()

    obj = BikeToUser.objects.filter(bike_id=id, status=True).first()
    obj.status = False
    obj.save()

    return redirect('bike:my-bike')
