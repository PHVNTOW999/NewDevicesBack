from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    path('meetlist/', MeetsViewList.as_view(), name='MeetList'),
    path('meet/<uuid:uuid>/', MeetView.as_view(), name='Meet'),
]