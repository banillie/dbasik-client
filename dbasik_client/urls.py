from django.contrib import admin
from django.urls import path
from datamap.views import (
    dbasik_api_view,
    home_view,
    datamaps_list_view,
    datamap_detail_view,
    datamap_line_edit,
)

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('dbasik-api/', dbasik_api_view, name='dbasik_api'),
    path('datamap-list/', datamaps_list_view, name='datamap-list'),
    path('datamap-detail/<int:pk>', datamap_detail_view, name='datamap-detail'),
    path('datamap-line-edit/<int:pk>', datamap_line_edit, name='datamap-line-edit')
]
