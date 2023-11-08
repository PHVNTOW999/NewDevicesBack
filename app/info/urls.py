from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    # meets
    path('meetlist/', MeetsViewList.as_view(), name='meet_list'),
    path('meet/<uuid:uuid>/', MeetView.as_view(), name='meet'),

    # phones
    path('phone/', PhoneView.as_view(), name='phone'),
    path('phone/<uuid:uuid>/', PhoneView.as_view(), name='phone'),

    # phones
    path('email/', EmailView.as_view(), name='email'),
    path('email/<uuid:uuid>/', EmailView.as_view(), name='email'),

    # clients
    path('clientslist/', ClientsListView.as_view(), name='clients_list'),
]