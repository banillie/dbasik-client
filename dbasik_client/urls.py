from django.contrib import admin
from django.urls import path
from datamap.views import dbasik_api_view, home_view

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('dbasik_api/', dbasik_api_view, name='dbasik_api')
]
