from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    #phones
    path('phonelist/', PhoneViewList.as_view(), name='phone_list'),
    # meets
    path('meetlist/', MeetsViewList.as_view(), name='meet_list'),
    path('meet/<uuid:uuid>/', MeetView.as_view(), name='meet'),

    # clients
    path('clientlist/', ClientViewList.as_view(), name='client_list'),
]