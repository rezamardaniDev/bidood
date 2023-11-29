from django.urls import path
from . import views
app_name = 'reservation'

urlpatterns = [
    path('get/<id>', views.get_bike, name='get-bike'),
    path('revert/<id>', views.revert_bike, name='revert-bike')
]
