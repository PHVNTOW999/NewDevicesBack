from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    # main
    path('admin/', admin.site.urls),
    path('api/curr/', Curr.as_view(), name='Currencies'),
    # info
    path('api/info/', include('info.urls', namespace='info'))
]
