from django.urls import path
from . import views

app_name = 'bike'

urlpatterns = [
    path('bike-list', views.ListBikeView.as_view(), name='bike-list'),
    path('my-bike', views.MyBikesView.as_view(), name='my-bike')
]
