from django.contrib import admin
from django.urls import path
from datamap.views import (
    dbasik_api_view,
    home_view,
    datamaps_list_view,
    datamap_detail_view,
)

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('dbasik_api/', dbasik_api_view, name='dbasik_api'),
    path('datamap_list/', datamaps_list_view, name='datamap-list'),
    path('datamap_detail/<int:pk>', datamap_detail_view, name='datamap-detail')
]
